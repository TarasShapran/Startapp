from rest_framework.serializers import ModelSerializer

from .models import AutoParkModel
from cars.serializers import CarSerializer


class AutoParkSerializer(ModelSerializer):
    cars = CarSerializer(many=True)

    class Meta:
        model = AutoParkModel
        fields = '__all__'

