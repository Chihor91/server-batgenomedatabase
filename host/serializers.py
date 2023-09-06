from rest_framework import serializers

from .models import Host
from taxonomy.serializers import TaxonomySerializer

class HostSerializer(serializers.ModelSerializer):
    host_taxonomy = TaxonomySerializer(many = False, required = True)
    class Meta:
        model = Host
        fields = '__all__'