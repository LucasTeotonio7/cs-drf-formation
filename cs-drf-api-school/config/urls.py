from django.contrib import admin
from django.urls import path, include

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
    path('student/<int:pk>/enrollments/', EnrollmentStudentListViewSet.as_view()),
    path('course/<int:pk>/enrollments/', ListStudentsEnrolledInCourseViewSet.as_view()),
]
