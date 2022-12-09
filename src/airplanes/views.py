from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Airplane
from .serializers import AirplaneSerializer, CreateListAirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()

    def get_serializer_class(self):
        if self.action == "create_list_airplane":
            return CreateListAirplaneSerializer
        return AirplaneSerializer

    @action(
        detail=False,
        methods=["post"],
        name="Create list airplane",
        url_path="create_list_airplane",
        url_name="create-list-airplane",
    )
    def create_list_airplane(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
        return Response({"data": response})
