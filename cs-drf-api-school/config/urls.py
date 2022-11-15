from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from apps.school.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, \
    EnrollmentStudentListViewSet, ListStudentsEnrolledInCourseViewSet


router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename="students")
router.register('courses', CourseViewSet, basename="courses")
router.register('enrollment', EnrollmentViewSet, basename="enrollment")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments/', EnrollmentStudentListViewSet.as_view()),
    path('courses/<int:pk>/enrollments/', ListStudentsEnrolledInCourseViewSet.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
