from rest_framework import viewsets

from apps.school.auth import AuthMixin
from apps.school.models import Course
from apps.school.serializers import CourseSerializer


class CourseViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
