from rest_framework import serializers

from api.models.productOrder import ProductOrder
from api.models.product import Product

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'