from rest_framework.response import Response
from rest_framework.views import APIView


class MyView(APIView):
    def get(self, *args, **kwargs):
        return Response({'msg': 'Hello from GET'})


    def post(self, *args, **kwargs):
        return Response({'msg': 'Hello from POST'})


    def put(self, *args, **kwargs):
        return Response({'msg': 'Hello from PUT'})


    def patch(self, *args, **kwargs):
        return Response({'msg': 'Hello from PATCH'})


    def delete(self, *args, **kwargs):
        return Response({'msg': 'Hello from DELETE'})
