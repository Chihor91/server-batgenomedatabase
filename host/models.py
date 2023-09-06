from django.db import models
from taxonomy.models import Taxonomy

# Create your models here.
class Host(models.Model):
    class Meta:
        verbose_name_plural = "hosts"

    common_name = models.CharField(max_length=100)
    host_type = models.CharField(max_length=50) #TODO: change to enum
    host_taxonomy = models.ForeignKey(Taxonomy, related_name="hosts", on_delete=models.CASCADE)

    def __str__(self):
        return self.host_taxonomy