from rest_framework import viewsets, status
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except:
            return Response(
                {'message': 'An error has occurred while creating isolate.'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )