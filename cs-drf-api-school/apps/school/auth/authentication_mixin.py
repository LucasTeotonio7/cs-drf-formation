from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class AuthMixin():
    pass
    # authentication_class = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
