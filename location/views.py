from rest_framework import viewsets

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

    serializer_class = LocationSerializer

class CaveViewSet(viewsets.ModelViewSet):
    queryset = Cave.objects.all()

    serializer_class = CaveSerializer

class SamplingPointViewSet(viewsets.ModelViewSet):
    queryset = SamplingPoint.objects.all()

    serializer_class = SamplingPointSerializer