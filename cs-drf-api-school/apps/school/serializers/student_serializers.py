from rest_framework import serializers
from apps.school.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'cpf', 'rg', 'birth_date', 'photo']


class StudentSerializerV2(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
