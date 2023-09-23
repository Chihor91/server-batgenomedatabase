from rest_framework import viewsets

# Create your views here.
from .serializers import (
    SourceSerializer,
    IsolateSerializer,
    ProjectSerializer
)

from .models import (
    Source,
    Isolate,
    Project
)

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()

    serializer_class = SourceSerializer

class IsolateViewSet(viewsets.ModelViewSet):
    queryset = Isolate.objects.all()

    serializer_class = IsolateSerializer

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer 