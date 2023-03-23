from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel


class CarsListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all().values()
        return Response(cars, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarModel.objects.create(**data)
        return Response(model_to_dict(car), status.HTTP_200_OK)


class CarsRetrieveUpdatesDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        is_exists = CarModel.objects.filter(pk=pk).exists()
        if not is_exists:
            return Response(f'User is id:{pk} not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        return Response(model_to_dict(car))

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        is_exists = CarModel.objects.filter(pk=pk).exists()
        if not is_exists:
            return Response(f'User is id:{pk} not found', status.HTTP_404_NOT_FOUND)
        CarModel.objects.filter(pk=pk).update(**data)
        return Response(f'Updated')

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        is_exists = CarModel.objects.filter(pk=pk).exists()
        if not is_exists:
            return Response(f'User is id:{pk} not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
