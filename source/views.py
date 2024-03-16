from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action


from django.shortcuts import get_object_or_404
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

    serializer_class = SourceSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except:
            return Response(
                {'message': 'An error has occurred while creating source.'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve(self, request, pk=None):
        print(pk)
        source = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(source)
        
        return Response(serializer.data)

class IsolateViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = Isolate.objects.all()

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
    
    @action(detail=True, methods=['get'], name='Get by ID')
    def get_by_id(self, request, pk=None):
        try:
            user = request.user
            if user.is_superuser:
                isolates = Isolate.objects.filter(source=pk)
            elif not user.is_anonymous:
                isolates = Isolate.objects.filter(Q(visibility="Public") | Q(visibility="Researchers Only") | Q(author_id = user.id), source=pk)
            else:
                isolates = Isolate.objects.filter(source=pk, visibility="Public")
            serializer = self.get_serializer(isolates, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(
                {'message': 'An error has occurred while adding isolate.'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    def retrieve(self, request, pk=None):
        user = request.user
        isolate = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(isolate)

        if (user.is_superuser 
            or serializer.data['author_id'] == user.id 
            or serializer.data['visibility'] == "Public" 
            or (serializer.data['visibility'] == "Researchers Only" 
                and not user.is_anonymous)):
            return Response(serializer.data)
        else: return Response(
            {'error': 'Isolate not found.'},
            status= status.HTTP_404_NOT_FOUND
        )

    def list(self, request):
        user = request.user
        if user.is_superuser:
            isolates = Isolate.objects.all()
        elif not user.is_anonymous:
            isolates = Isolate.objects.filter(Q(visibility="Public") | Q(visibility="Researchers Only") | Q(author_id = user.id))
        else:
            isolates = Isolate.objects.filter(visibility="Public")

        serializer = self.get_serializer(isolates, many=True)
        return Response(serializer.data)