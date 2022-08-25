from rest_framework import serializers

from api.models.customer import Customer

class CustomerSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['id']

    def validate_first_name(self, value):
        if (len(value) < 2):
            raise serializers.ValidationError('Name is too short')
        return value

    def get_full_name(self, object):
        return f'{object.first_name} {object.last_name}'
