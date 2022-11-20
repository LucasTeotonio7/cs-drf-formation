from rest_framework import viewsets, filters
from aluraflix.serializers import ProgramSerializer
from aluraflix.models import Program
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    # print(str(queryset.query))
    serializer_class = ProgramSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['type']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

