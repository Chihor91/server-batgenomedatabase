from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
import csv
import codecs

# Create your views here.
from .serializers import (
    SourceSerializer,
    IsolateSerializer
)

from .models import (
    Source,
    Isolate
)

from user.models import Account
from django.db.models import Q 

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    serializer_class = SourceSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except:
            return Response(
                {'message': 'An error has occurred while creating source.'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class IsolateViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Isolate.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','source']

    serializer_class = IsolateSerializer

    def create(self, request, *args, **kwargs):
        try:
            if Account.objects.filter(id=request.user.id).exists():
                request.data["author_id"] = request.user.id
                request.data["author"] = request.user.username
                return super().create(request, *args, **kwargs)
            else:   return Response(
                {'error': 'User not authenticated.'},
                status = status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            print(e)
            return Response(
                {'message': 'An error has occurred while adding isolate.'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    @action(detail=False, methods=['POST'], name='Import from file')
    def import_from_file(self, request, *args, **kwargs):
        file = request.data['isolates']
        reader = csv.DictReader(codecs.iterdecode(file, 'utf-8'))
        for row in reader:
            print(row['SOURCE'])
        return(Response(status = status.HTTP_200_OK))
        
    def list(self, request):
        user = request.user
        print(user)
        if user.is_superuser:
            isolates = Isolate.objects.all()
        elif not user.is_anonymous:
            print("Authenticated")
            isolates = Isolate.objects.filter(Q(visibility="Public") | Q(visibility="Researchers Only") | Q(author_id = user.id))
        else:
            isolates = Isolate.objects.filter(visibility="Public")

        serializer = self.get_serializer(isolates, many=True)
        return Response(serializer.data)