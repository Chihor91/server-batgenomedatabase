from rest_framework import serializers

from .models import (
    Domain, 
    Phylum, 
    Class, 
    Order, 
    Family, 
    Genus, 
    Species
    )

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'
        
class PhylumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phylum
        fields = '__all__'
                
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
                
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'
        
class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = '__all__'
                
class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'