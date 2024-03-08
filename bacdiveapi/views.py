from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import bacdive

# client = bacdive.BacdiveClient('ngarcia@up.edu.ph', 'popowhee123')

# Create your views here.
class TestView(APIView):
    def get(self, request, format=None):
        strains = []
        client = bacdive.BacdiveClient('ngarcia@up.edu.ph', 'popowhee123')
        client.setSearchType('exact')
        # query = {"taxonomy": ("Peptostreptococcus", "anaerobius")}
        query = {"id": 11843}
        client.search(**query)
        
        for strain in client.retrieve():
            strains.append(strain)

        return Response(strains, status=status.HTTP_200_OK)