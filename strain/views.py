from django.shortcuts import render
from rest_framework import viewsets

from .serializers import (
    TaxonomySerializer,
    StrainSerializer
)

from .models import (
    Taxonomy,
    Strain
)

# Create your views here.

class TaxonomyViewSet(viewsets.ModelViewSet):
    queryset = Taxonomy.objects.all()

    serializer_class = TaxonomySerializer

class StrainViewSet(viewsets.ModelViewSet):
    queryset = Strain.objects.all()

    serializer_class = StrainSerializer