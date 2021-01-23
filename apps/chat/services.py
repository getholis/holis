import uuid

from typing import Any, Dict, List

from django.core.files.storage import default_storage
from channels.db import database_sync_to_async

from ..chat import models as chat_models
from .providers import room as room_providers
from ..chat.api import serializers
from apps.users import models as users_models


class NonExistentMemberException(Exception):
    pass


@database_sync_to_async
def create_message(
    company_id: int, user_id: int, room_id: int, text: str
) -> chat_models.Message:
    return chat_models.Message.objects.create(
        company_id=company_id, room_id=room_id, user_id=user_id, text=text
    )


@database_sync_to_async
def serialize_message(message: chat_models.Message) -> Dict[str, Any]:

    data = serializers.MessageSerializer(message).data

    # This is a patch to Django Serializer BUG
    # https://stackoverflow.com/questions/36588126/uuid-is-not-json-serializable

    data["id"] = str(data["id"])
    data["room"] = str(data["room"])
    data["type"] = "chat.message"
    return data


def get_recents_rooms(user_id: id) -> Dict[str, Any]:
    rooms_ids = (
        chat_models.Message.objects.filter(
            room__is_one_to_one=True,
            room__members__id=user_id,
        )
        .order_by("room__id", "-created")
        .distinct("room__id")
        .values_list("room__id", flat=True)
    )[:3]

    rooms_data = (
        chat_models.Room.objects.filter(id__in=rooms_ids)
        .prefetch_related("members")
        .values("id", "members__avatar", "members__id", "members__name")
    )

    return [
        {
            "room": x["id"],
            "avatar_thumb": default_storage.url(x["members__avatar"]),
            "id": x["members__id"],
            "name": x["members__name"],
        }
        for x in rooms_data
        if x["members__id"] != user_id
    ]


def get_or_create_room_by_company_and_members_ids(company_id: int, members_ids: List[int]) -> chat_models.Room:
    try:
        return room_providers.get_one_to_one_room_by_members_ids(
            company_id=company_id,
            members_ids=members_ids
        )
    except chat_models.Room.DoesNotExist:
        pass

    channel = chat_models.Room.objects.create(
        **{
            "company_id": company_id,
            "is_one_to_one": True,
            "name": str(uuid.uuid4()),
            "any_can_invite": False,
            "members_only": True,
            "max_users": 2,
        }
    )

    members = users_models.User.objects.filter(
        id__in=members_ids, company_id=company_id
    )

    if members.count() != len(members_ids):
        raise NonExistentMemberException("User does not exist")

    for member in members:
        channel.members.add(member)
