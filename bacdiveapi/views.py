from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import bacdive

client = bacdive.BacdiveClient('ngarcia@up.edu.ph', 'popowhee123')

# Create your views here.
class TestView(APIView):
    def get(self, request, format=None):
        strains = []
        client.setSearchType('exact')
        query = {"genome": ["GCA_003332855", "GCA_024623325", "GCA_017377855"]}
        client.search(**query)
        
        for strain in client.retrieve():
            strains.append(strain)

        return Response(strains, status=status.HTTP_200_OK)