from django.db import transaction
from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from .models import Airplane
from .validations import validate_passengers


class AirplaneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    passengers = serializers.IntegerField(validators=[validate_passengers])
    fuel_tanks_capacity = serializers.ReadOnlyField()
    fuel_consumption_per_minutes = serializers.ReadOnlyField()
    maximum_minutes_able_to_fly = serializers.ReadOnlyField()

    class Meta:
        model = Airplane
        fields = (
            "id",
            "passengers",
            "fuel_tanks_capacity",
            "fuel_consumption_per_minutes",
            "maximum_minutes_able_to_fly",
        )


class CreateListAirplaneSerializer(serializers.Serializer):
    airplanes = AirplaneSerializer(many=True)

    @transaction.atomic
    def create(self, validated_data: dict) -> ReturnDict:
        result = []
        for airplane in validated_data["airplanes"]:
            try:
                obj = Airplane.objects.get(pk=airplane.get("id"))
                obj.passengers = airplane["passengers"]
                obj.save()
            except Airplane.DoesNotExist:
                obj = Airplane.objects.create(passengers=airplane["passengers"])

            result.append(obj)

        return AirplaneSerializer(result, many=True).data
