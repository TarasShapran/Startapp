from rest_framework.serializers import ModelSerializer

from .models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

    def validate(self, date):

        return super().validate(date)


class Car2Serializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand')
