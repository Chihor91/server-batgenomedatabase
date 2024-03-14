from rest_framework import serializers

from .models import (
    Source,
    Isolate
)

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"

class IsolateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isolate
        fields = "__all__"