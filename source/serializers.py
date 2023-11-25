from rest_framework import serializers

from .models import (
    Source,
    Strain
)

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"

class StrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strain
        fields = "__all__"