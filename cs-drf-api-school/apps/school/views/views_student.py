from rest_framework import viewsets

from apps.school.auth import AuthMixin
from apps.school.models import Student
from apps.school.serializers import StudentSerializer


class StudentViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
