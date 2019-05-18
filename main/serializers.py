from rest_framework import serializers
from django.forms.models import model_to_dict
from .models import CenterModel, CenterDistanceModel, ProductModel, LoadModel, LoadDistanceModel, OrderModel


class CenterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterModel
        fields = '__all__'


class CenterDistanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterDistanceModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class LoadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadModel
        fields = '__all__'


class LoadDistanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadDistanceModel
        fields = '__all__'


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'