from django.contrib.auth import get_user_model

import pytest

from ..api.v100 import serializers
from .baker_recipes import user_viktor

User = get_user_model()


@pytest.mark.django_db()
def test_serialize_queryzet_contract():
    user = user_viktor.make()
    queryset = User.objects.all().order_by("id")

    serialized = serializers.serialize_user_queryset(queryset)

    assert User.objects.count() == 1
    assert isinstance(serialized["results"], list)
    assert serialized["results"][0]["id"] == user.id
