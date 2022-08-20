from rest_framework import serializers

from api.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'