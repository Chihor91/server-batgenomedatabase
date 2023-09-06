from rest_framework import serializers

from .models import Strain

from taxonomy.serializers import TaxonomySerializer

class StrainSerializer(serializers.ModelSerializer):
    taxonomy = TaxonomySerializer()
    class Meta:
        model = Strain
        fields = '__all__'
        