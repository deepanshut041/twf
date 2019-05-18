from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import CenterModel, CenterDistanceModel, ProductModel, LoadModel, LoadDistanceModel, OrderModel
from .serializers import (CenterModelSerializer, CenterDistanceModelSerializer, ProductModelSerializer,
                             LoadModelSerializer, LoadDistanceModelSerializer, OrderModelSerializer)

# Create your views here.
class CenterView(ModelViewSet):
    queryset = CenterModel.objects.all()
    serializer_class = CenterModelSerializer

class CenterDistanceView(ModelViewSet):
    queryset = CenterDistanceModel.objects.all()
    serializer_class = CenterDistanceModelSerializer

class ProductView(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer

class LoadView(ModelViewSet):
    queryset = LoadModel.objects.all()
    serializer_class = LoadModelSerializer


class LoadDistanceView(ModelViewSet):
    queryset = LoadDistanceModel.objects.all()
    serializer_class = LoadDistanceModelSerializer

class OrderView(ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer

