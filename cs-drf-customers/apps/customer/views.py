from rest_framework import viewsets
from apps.customer.serializers import CustomerSerializer
from apps.customer.models import Customer

class CustomerViewSet(viewsets.ModelViewSet):
    """customer list"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
