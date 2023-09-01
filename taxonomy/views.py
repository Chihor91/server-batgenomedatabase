from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny

from .serializers import (
    DomainSerializer, 
    PhylumSerializer, 
    ClassSerializer, 
    OrderSerializer, 
    FamilySerializer, 
    GenusSerializer, 
    SpeciesSerializer,
    )
from .models import (
    Domain,
    Phylum,
    Class,
    Order,
    Family,
    Genus,
    Species,
)
# Create your views here.

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    permission_classes = [AllowAny]

    serializer_class = DomainSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]

class PhylumViewSet(viewsets.ModelViewSet):
    queryset = Phylum.objects.all()

    serializer_class = PhylumSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()

    serializer_class = ClassSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    serializer_class = OrderSerializer

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()

    serializer_class = FamilySerializer

class GenusViewSet(viewsets.ModelViewSet):
    queryset = Genus.objects.all()

    serializer_class = GenusSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()

    serializer_class = SpeciesSerializer
