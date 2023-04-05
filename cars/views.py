from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel
from .serializers import CarSerializer, Car2Serializer


class CarsListCreateView(APIView):
    def get(self, *args, **kwargs):
        # cars = CarModel.objects.filter(year__gte='2015-06-06')
        # cars = CarModel.objects.filter(year__lte='2015-06-06')
        # cars = CarModel.objects.filter(year__exact='2015-06-06')
        # cars = CarModel.objects.filter(year__year='2015-06-06')
        cars = CarModel.objects.all()
        serializer = CarSerializer(instance=cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class CarsRetrieveUpdatesDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        is_exists = CarModel.objects.filter(pk=pk).exists()
        if not is_exists:
            return Response(f'Car is id:{pk} not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        serializer = Car2Serializer(instance=car)
        return Response(serializer.data)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        is_exists = CarModel.objects.filter(pk=pk).exists()
        if not is_exists:
            return Response(f'Car is id:{pk} not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(instance=car, data=data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        is_exists = CarModel.objects.filter(pk=pk).exists()
        if not is_exists:
            return Response(f'User is id:{pk} not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
