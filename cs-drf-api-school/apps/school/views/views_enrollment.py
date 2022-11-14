from rest_framework import viewsets, generics

from apps.school.auth import AuthMixin
from apps.school.models import Enrollment
from apps.school.serializers import EnrollmentSerializer, EnrollmentStudentListSerializer, \
    ListStudentsEnrolledInCourseSerializer


class EnrollmentViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


class EnrollmentStudentListViewSet(AuthMixin, generics.ListAPIView):
    serializer_class = EnrollmentStudentListSerializer

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset


class ListStudentsEnrolledInCourseViewSet(AuthMixin, generics.ListAPIView):
    serializer_class = ListStudentsEnrolledInCourseSerializer

    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
