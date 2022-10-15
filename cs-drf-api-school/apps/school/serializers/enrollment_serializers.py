from rest_framework import serializers
from apps.school.models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = '__all__'


class EnrollmentStudentListSerializer(serializers.ModelSerializer):

    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()


class ListStudentsEnrolledInCourseSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Enrollment
        fields = ['student']
