from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from .serializers import (
    SourceSerializer,
    StrainSerializer
)

from .models import (
    Source,
    Strain
)

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    serializer_class = SourceSerializer

class StrainViewSet(viewsets.ModelViewSet):
    queryset = Strain.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','source']

    serializer_class = StrainSerializer