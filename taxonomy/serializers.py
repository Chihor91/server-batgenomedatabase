from rest_framework import serializers

from .models import Domain, Phylum, Class, Order, Family, Genus, Species

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        field = '__all__'
        