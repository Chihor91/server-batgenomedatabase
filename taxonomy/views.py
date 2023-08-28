from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import DomainSerializer
from .models import Domain
# Create your views here.

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
