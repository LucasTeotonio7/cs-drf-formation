from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AuthMixin():
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
