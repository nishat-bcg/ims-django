from rest_framework import serializers

from api.models.customerGroup import CustomerGroup

class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroup
        fields = '__all__'