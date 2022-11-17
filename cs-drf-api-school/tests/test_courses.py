from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from apps.school.models import Course



class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse('courses-list')
        self.course1 = Course.objects.create(
            code="TEST-1", 
            description="Course test 1", 
            level=Course.Level.BASIC
        )
        self.course2 = Course.objects.create(
            code="TEST-2", 
            description="Course test 2", 
            level=Course.Level.INTERMEDIARY
        )
    
    def test_get_request_to_list_courses(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request_to_create_course(self):
        data = {
            "code":"TEST-3", 
            "description":"Course test 3", 
            "level": Course.Level.ADVANCED
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_request_to_update_course(self):
        data = {
            "code":"TEST-1", 
            "description":"Course test 1 update", 
            "level": Course.Level.INTERMEDIARY
        }
        response = self.client.put('/courses/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_to_delete_course(self):
        response = self.client.delete('/courses/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
