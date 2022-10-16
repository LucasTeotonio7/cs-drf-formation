from rest_framework import serializers
from apps.customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError('O cpf deve ter 11 dígitos.')
        return value
