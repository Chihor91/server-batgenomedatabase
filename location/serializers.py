from rest_framework import serializers

from .models import (
    Location,
    Cave,
    SamplingPoint
)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cave
        fields = '__all__'

class SamplingPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamplingPoint
        fields = '__all__'