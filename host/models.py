from django.db import models

# Create your models here.
class Host(models.Model):
    type = models.CharField(max_length=50) #TODO: change to enum
    species = models.CharField(max_length=255)

    def __str__(self):
        return self.species
    
class Sample(models.Model):
    type = models.CharField(max_length=50)
    host = models.ForeignKey(Host, related_name="samples", on_delete=models.CASCADE)

    def __str__(self):
        return self.type

