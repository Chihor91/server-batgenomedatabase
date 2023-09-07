from django.db import models
from taxonomy.models import Taxonomy

# Create your models here.
class Host(models.Model):
    host_name = models.CharField(max_length=255)
    host_type = models.CharField(max_length=50) #TODO: change to enum
    host_species = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Sample(models.Model):
    sample_type = models.CharField(max_length=50)

    def __str__(self):
        return self.sample_type