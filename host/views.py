from django.shortcuts import render
from rest_framework import viewsets

from .models import Host

from .serializers import HostSerializer

# Create your views here.

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()

    serializer_class = HostSerializer