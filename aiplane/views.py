from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AirPlaneModel
from .serializers import AirPlaneSerializer, AirPlaneSerializerEdit


class AirPlaneListCreateView(APIView):
    def get(self, *args, **kwargs):
        airplane = AirPlaneModel.objects.all()
        serializer = AirPlaneSerializer(airplane, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        plane_serializer = AirPlaneSerializer(data=data)
        plane_serializer.is_valid(raise_exception=True)
        plane_serializer.save()
        return Response(plane_serializer.data, status.HTTP_201_CREATED)


class AirPlaneRetriveUpdateView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        airplane = AirPlaneModel.objects.filter(pk=pk).exists()
        if not airplane:
            return Response(status=status.HTTP_404_NOT_FOUND)
        airplane = AirPlaneModel.objects.get(pk=pk)
        plane_serializer = AirPlaneSerializer(airplane)
        return Response(plane_serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        is_exist = AirPlaneModel.objects.filter(pk=pk).exists()
        if not is_exist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        airplane = AirPlaneModel.objects.get(pk=pk)
        serializer = AirPlaneSerializerEdit(airplane, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        is_exist = AirPlaneModel.objects.filter(pk=pk).exists()
        if not is_exist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        airplane = AirPlaneModel.objects.get(pk=pk)
        serializer = AirPlaneSerializerEdit(airplane, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = AirPlaneModel.objects.filter(pk=pk).exists()
        if not data:
            return Response(status=status.HTTP_404_NOT_FOUND)
        airplane = AirPlaneModel.objects.get(pk=pk)
        airplane.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
