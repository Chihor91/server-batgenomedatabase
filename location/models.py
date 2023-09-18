from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Location(models.Model):
    location_abbr = models.CharField(max_length=50)
    location_province = models.CharField(max_length=255)
    location_town = models.CharField(max_length=255)
    location_long = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    location_lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])

    def __str__(self):
        return self.location_abbr

class SamplingSite(models.Model):
    site_abbr = models.CharField(max_length=50)
    site_name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, related_name='sites', on_delete=models.CASCADE)

    def __str__(self):
        return self.site_abbr
    
class SamplingPoint(models.Model):
    point_number = models.AutoField(primary_key=True)
    sampling_site = models.ForeignKey(SamplingSite, related_name='points', on_delete=models.CASCADE)

    def __str__(self):
        return self.point_number