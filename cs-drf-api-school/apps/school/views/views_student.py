from rest_framework import viewsets

from apps.school.auth import AuthMixin
from apps.school.models import Student
from apps.school.serializers import StudentSerializer, StudentSerializerV2


class StudentViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        else:
            return StudentSerializer
