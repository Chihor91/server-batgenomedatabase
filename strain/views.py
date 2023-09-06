from django.shortcuts import render
from rest_framework import viewsets

from .models import Strain
from .serializers import StrainSerializer

# Create your views here.
class StrainViewSet(viewsets.ModelViewSet):
    queryset = Strain.objects.all()
    
    serializer_class = StrainSerializer