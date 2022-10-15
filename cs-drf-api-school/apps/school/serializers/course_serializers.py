from rest_framework import serializers
from apps.school.models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
