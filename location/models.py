from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Location(models.Model):
    abbr = models.CharField(max_length=25)
    province = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    long = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])

    def __str__(self):
        return self.abbr

class Cave(models.Model):
    abbr = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, related_name='caves', on_delete=models.CASCADE)

    def __str__(self):
        return self.abbr
    
class SamplingPoint(models.Model):
    point_number = models.IntegerField(blank=True, default=0)
    cave = models.ForeignKey(Cave, related_name='points', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.point_number = self.cave.points.count()
        super(SamplingPoint, self).save(*args, **kwargs)
        

    def __str__(self):
        return str(self.point_number)