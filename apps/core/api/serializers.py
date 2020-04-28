from rest_framework import serializers
from apps.core import models as core_models
from apps.core.uc.area_uc import GetStateAreaUC


class CustomCurrentCompany(serializers.CurrentUserDefault):
    def __call__(self, serializer_field):
        _id: int = serializer_field.context["request"].user.company_id
        return core_models.Company.objects.get(id=_id)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Company
        fields = "__all__"


class StateField(serializers.ReadOnlyField):
    def to_representation(self, obj):
        state = GetStateAreaUC(obj).execute()
        return state


class AreaSerializer(serializers.ModelSerializer):
    company = serializers.HiddenField(default=CustomCurrentCompany())
    state = StateField()

    class Meta:
        model = core_models.Area
        fields = "__all__"
