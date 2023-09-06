from django.shortcuts import render
from rest_framework import viewsets

from .serializers import IsolateSerializer
from .models import Isolate

# Create your views here.

class IsolateViewSet(viewsets.ModelViewSet):
    queryset = Isolate.objects.all()

    serializer_class = IsolateSerializer