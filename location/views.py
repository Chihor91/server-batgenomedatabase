from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    LocationSerializer,
    CaveSerializer,
    SamplingPointSerializer
)

from .models import (
    Location,
    Cave,
    SamplingPoint
)

# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    serializer_class = LocationSerializer

class CaveViewSet(viewsets.ModelViewSet):
    queryset = Cave.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location']

    serializer_class = CaveSerializer

class SamplingPointViewSet(viewsets.ModelViewSet):
    queryset = SamplingPoint.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cave']

    serializer_class = SamplingPointSerializer