from rest_framework import serializers

from .models import (
    Source,
    Isolate,
    Project
)

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"

class IsolateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isolate
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"