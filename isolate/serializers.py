from rest_framework import serializers

from .models import Isolate

class IsolateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isolate
        fields = '__all__'