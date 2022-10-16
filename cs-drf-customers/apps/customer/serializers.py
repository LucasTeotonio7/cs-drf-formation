from rest_framework import serializers
from apps.customer.models import Customer
from apps.customer.validators import validate_min_length, list_in_one_dict

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('Não inclua dígitos nesse campo.')
        return value

    def validate(self, data):
        print("cpf")
        errors_list = []

        errors_list.append(validate_min_length('cpf', data.get('cpf'), 11))
        errors_list.append(validate_min_length('rg', data.get('rg'), 9))
        errors_list.append(validate_min_length('phone', data.get('phone'), 12))

        qty_errors = 0
        for error in errors_list:
            if error is not None:
                qty_errors =+ 1

        if qty_errors > 0:
            raise serializers.ValidationError(list_in_one_dict(errors_list))
        return data
