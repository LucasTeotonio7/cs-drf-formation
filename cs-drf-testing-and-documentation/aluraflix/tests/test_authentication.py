from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programs-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_authentication_with_correct_credentials(self):
        user = authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_authentication_with_incorrect_username(self):
        user = authenticate(username='c3pp', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authentication_with_incorrect_password(self):
        user = authenticate(username='c3po', password='123455')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_unauthorized_request(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
