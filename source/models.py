from django.db import models
from location.models import SamplingPoint
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbr = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.abbr



class Source(models.Model):
    collection = models.CharField(max_length=25)
    institution = models.CharField(max_length=50)
    type = models.IntegerField()    # 1 - Bacteria, 2 = Yeast, 3 = Mold
    type_id = models.IntegerField(blank=True)
    
    host_type = models.CharField(max_length=25, blank=True) 
    host_species = models.CharField(max_length=50, blank=True)
    sample_type = models.CharField(max_length=25)

    accession_no = models.CharField(max_length=100, blank=True)

    human_readable_id = models.CharField(max_length=150, blank=True)

    project = models.ForeignKey(Project, related_name='sources', on_delete=models.CASCADE, blank=True)
    sampling_point = models.ForeignKey(SamplingPoint, related_name='sources', on_delete=models.SET_NULL, null=True)


    def save(self, *args, **kwargs):
        self.type_id = (self.type + 4) * 10000 + (Source.objects.filter(type=self.type).count() + 1)
        self.accession_no = '-'.join([self.collection, self.institution, str(self.type_id)]) 
        self.human_readable_id = '-'.join([self.collection, self.institution, self.project.abbr, self.sampling_point.cave.location.abbr, self.sampling_point.cave.abbr, str(self.sampling_point.point_number), str(self.type), self.host_type, self.sample_type])
        super(Source, self).save(*args, **kwargs)

    def __str__(self):
        return self.accession_no
    
class Isolate(models.Model):
    human_readable_id = models.CharField(max_length=150, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Isolate, self).save(*args, **kwargs)
        self.human_readable_id = '-'.join([self.source.human_readable_id, str(self.id).zfill(5)])
        super(Isolate, self).save(*args, **kwargs)

    def __str__(self):
        return self.human_readable_id