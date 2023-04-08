from rest_framework import serializers
from vacation.models import Vacation


class VacationSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        model=Vacation
        fields='__all__'