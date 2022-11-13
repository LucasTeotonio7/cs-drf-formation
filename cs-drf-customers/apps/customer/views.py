from rest_framework import viewsets, filters
from apps.customer.serializers import CustomerSerializer
from apps.customer.models import Customer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):
    """customer list"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter ]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    filterset_fields = ['active']
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

