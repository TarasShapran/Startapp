from rest_framework.serializers import ModelSerializer

from .models import AirPlaneModel


class AirPlaneSerializer(ModelSerializer):
    class Meta:
        model = AirPlaneModel
        fields = '__all__'


class AirPlaneSerializerEdit(ModelSerializer):
    class Meta:
        model = AirPlaneModel
        fields = ['name', 'speed', 'engine']
