from rest_framework import serializers

from .models import (
    Taxonomy,
    Domain,
    Kingdom,
    Phylum, 
    Class, 
    Order, 
    Family, 
    Genus, 
    Species
    )

class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'

class GenusSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer(many=True, required=False)
    class Meta:
        model = Genus
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    genera = GenusSerializer(many=True, required=False)
    class Meta:
        model = Family
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    families = FamilySerializer(many=True, required=False)
    class Meta:
        model = Order
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, required=False)
    class Meta:
        model = Class
        fields = '__all__'

class PhylumSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source="parent.name", read_only=True, required=False)
    classes = ClassSerializer(many=True, required=False)
    class Meta:
        model = Phylum
        fields = '__all__'

class KingdomSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source="parent.name", read_only=True, required=False)
    phyla = PhylumSerializer(many=True, required=False)
    class Meta:
        model = Kingdom
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    
    Kingdoms = KingdomSerializer(many=True, required=False)
    class Meta:
        model = Domain
        fields = '__all__'
