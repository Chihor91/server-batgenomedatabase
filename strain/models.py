from django.db import models
from taxonomy.models import Taxonomy

# Create your models here.
class Strain(models.Model):
    class Meta:
        verbose_name_plural = "Strains"
    
    name = models.CharField(max_length=200)
    taxonomy = models.ForeignKey(Taxonomy, related_name='strains', on_delete=models.CASCADE)

    def __str__(self):
        return self.name