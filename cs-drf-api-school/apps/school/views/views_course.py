from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.school.auth import AuthMixin
from apps.school.models import Course
from apps.school.serializers import CourseSerializer


class CourseViewSet(AuthMixin, viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
