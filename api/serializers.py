from rest_framework import serializers
from api import models


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ShopModel
        fields = ['name']


class SupplierSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SupplierModel
        fields = ['name', 'address']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['shops_detail'] = ShopSerializers(instance.shop, many=True).data
        return response


class ReportsOfSupplierSerializers(serializers.Serializer):
    email = serializers.EmailField()
