from rest_framework import serializers

from api.models.productOrder import ProductOrder
from api.models.product import Product

class ProductOrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    product = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProductOrder
        fields = '__all__'