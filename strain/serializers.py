from rest_framework import serializers

from .models import (
    Taxonomy,
    Strain
)

class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = "__all__"

class StrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strain
        fields = "__all__"