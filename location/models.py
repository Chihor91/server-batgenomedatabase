from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=255)

class SamplingSite(models.Model):
    site_name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, related_name='sites', on_delete=models.CASCADE)

class SamplingPoint(models.Model):
    point_number = models.IntegerField()
    sampling_site = models.ForeignKey(SamplingSite, related_name='points', on_delete=models.CASCADE)