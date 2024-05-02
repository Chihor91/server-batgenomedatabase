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
    
    def source_count(self, request, *args, **kwargs):
        return Response(Source.objects.all().count())

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
        results = []
        for row in reader:
            try:
                # SOURCE
                source = Source.objects.get(human_readable_id=row['SOURCE'])

                # ISOLATE TYPE
                if row['ISOLATE_TYPE'].strip() == "Bacteria": type = 1
                elif row['ISOLATE_TYPE'].strip() == "Yeast": type = 2
                elif row['ISOLATE_TYPE'].strip() == "Mold": type = 3
                else: raise ValueError('Invalid isolate type.')

                # TAXONOMY
                taxonomy = {}
                if row['TAX_DOMAIN'].strip() != "": taxonomy['domain'] = row['TAX_DOMAIN']
                if row['TAX_PHYLUM'].strip() != "": taxonomy['phylum'] = row['TAX_PHYLUM']
                if row['TAX_CLASS'].strip() != "": taxonomy['class'] = row['TAX_CLASS']
                if row['TAX_ORDER'].strip() != "": taxonomy['order'] = row['TAX_ORDER']
                if row['TAX_FAMILY'].strip() != "": taxonomy['family'] = row['TAX_FAMILY']
                if row['TAX_GENUS'].strip() != "": taxonomy['genus'] = row['TAX_GENUS']
                if row['TAX_SPECIES'].strip() != "": taxonomy['species'] = row['TAX_SPECIES']

                # MORPHOLOGY
                morphology = {}
                
                gram_stain = row['MORPH_GRAM_STAIN']
                if gram_stain.strip() != "":
                    if gram_stain.strip() == "Gram-positive": morphology['gram_stain'] = True
                    elif gram_stain.strip() == "Gram-negative": morphology['gram_stain'] = False
                    else: raise ValueError("Invalid gram stain value.")

                cell_shape = row['MORPH_CELL_SHAPE']
                if cell_shape.strip() != "": morphology['cell_shape'] = cell_shape

                motility = row['MORPH_MOTILITY']
                if motility.strip() != "":
                    if motility.strip() == "yes": morphology['motility'] = True
                    elif motility.strip() == "no": morphology['motility'] = False
                    else: raise ValueError("Invalid motility value.")

                # CULTURE GROWTH
                culture_growth = {}
                
                medium = row['CULTURE_MEDIUM']
                if medium.strip() != "": culture_growth['medium'] = medium

                growth = row['CULTURE_MEDIUM_GROWTH']
                if growth.strip() != "":
                    if growth.strip() == "yes": culture_growth['growth'] = True
                    elif growth.strip() == "no": culture_growth['growth'] = False
                    else: raise ValueError("Invalid medium growth value.")

                medium_composition = row['CULTURE_MEDIUM_COMPOSITION']
                if medium_composition.strip() != "": culture_growth['medium_composition'] = medium_composition

                culture_temp = row['CULTURE_GROWTH_TEMPERATURE']
                if culture_temp.strip() != "": culture_growth['culture_temp'] = culture_temp

                temp_range = row['CULTURE_TEMPERATURE_RANGE']
                if temp_range.strip() != "": culture_growth['temp_range'] = temp_range

                # PHYSIOLOGY
                physiology_metabolism = {}

                oxygen_tolerance = row['PHYSIOLOGY_OXYGEN_TOLERANCE']
                if oxygen_tolerance.strip() != "": physiology_metabolism['oxygen_tolerance'] = oxygen_tolerance

                cytochrome_oxidase = row['PHYSIOLOGY_CYTOCHROME_C_OXIDASE_PRESENCE']
                if cytochrome_oxidase.strip() != "":
                    if cytochrome_oxidase.strip() == "Oxidase-positive": physiology_metabolism['cytochrome_oxidase'] = True
                    elif cytochrome_oxidase.strip() == "Oxidase-negative": physiology_metabolism['cytochrome_oxidase'] = False
                    else: raise ValueError("Invalid cytochrome c oxidase presence value")

                endospore_forming = row['PHYSIOLOGY_ENDOSPORE_FORMING_CAPABILITY']
                if endospore_forming.strip() != "":
                    if endospore_forming.strip() == "Endospore-forming": physiology_metabolism['endospore_forming'] = True
                    elif endospore_forming.strip() == "Non-endospore-forming": physiology_metabolism['endospore_forming'] = False
                    else: raise ValueError("Invalid endospore-forming-capability value")

                antibiotic_resistance_profile = row['PHYSIOLOGY_ANTIBIOTIC_RESISTANCE_PROFILE']
                if antibiotic_resistance_profile.strip() != "": physiology_metabolism['antibiotic_resistance_profile'] = antibiotic_resistance_profile

                # SAFETY
                safety_information = {}
                
                pathogenicity_human = row['SAFETY_PATHOGENICITY_HUMAN']
                if pathogenicity_human.strip() != "": safety_information['pathogenicity_human'] = pathogenicity_human

                pathogenicity_animal = row['SAFETY_PATHOGENICITY_ANIMAL']
                if pathogenicity_animal.strip() != "": safety_information['pathogenicity_animal'] = pathogenicity_animal

                biosafety_level = row['SAFETY_BIOSAFETY_LEVEL']
                if biosafety_level.strip() != "":  safety_information['biosafety_level'] = biosafety_level

                # VISIBILITY
                visibility = row['VISIBILITY']
                if visibility not in ["Public", "Researchers Only", "Private"]:
                    raise ValueError('Invalid visibility value.')
                
                author = request.user.username
                author_id = Account.objects.get(id=request.user.id)

                isolate = Isolate.objects.create(source=source, type=type, 
                                       taxonomy=taxonomy, morphology=morphology, 
                                       culture_growth=culture_growth, safety_information=safety_information, 
                                       visibility=visibility, author=author, author_id=author_id)
                print(isolate.human_readable_id)
                results.append({'success': True, 'message': "Isolate successfully added."})
            except Source.DoesNotExist:
                results.append({'success': False, 'message': "Source with specified human readable ID does not exist."})
            except ValueError as e:
                results.append({'success': False, 'message': e})
        print(results)
        return(Response({'results': results}, status = status.HTTP_201_CREATED))
    
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
        
    def isolate_count(self, request, *args, **kwargs):
        return Response(Isolate.objects.all().count())

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
    
    def destroy(self, request, pk=None, *args, **kwargs):
        user = request.user
        isolate = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(isolate)

        if (user.is_superuser or user.id == serializer.data['author_id']):
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(
                {'error': 'Unauthorized'},
                status=status.HTTP_401_UNAUTHORIZED
            )