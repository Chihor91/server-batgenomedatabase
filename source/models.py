from django.db import models
from location.models import SamplingPoint
# Create your models here.

class Source(models.Model):
    collection = models.CharField(max_length=25)
    institution = models.CharField(max_length=50)
    

    
    host_type = models.CharField(max_length=25, blank=True) 
    host_species = models.CharField(max_length=50, blank=True)
    sample_type = models.CharField(max_length=25)

    project_name = models.CharField(max_length=50)
    project_abbr = models.CharField(max_length=25)

    human_readable_id = models.CharField(max_length=150, blank=True)

    #project = models.ForeignKey(Project, related_name='sources', on_delete=models.CASCADE, blank=True)
    sampling_point = models.ForeignKey(SamplingPoint, related_name='sources', on_delete=models.SET_NULL, null=True)


    def save(self, *args, **kwargs):
        if (self.host_type == ""):
            self.human_readable_id = '-'.join([self.collection, self.institution, self.project_abbr, self.sampling_point.cave.location.abbr, self.sampling_point.cave.abbr, str(self.sampling_point.point_number), self.sample_type])
        else: 
            self.human_readable_id = '-'.join([self.collection, self.institution, self.project_abbr, self.sampling_point.cave.location.abbr, self.sampling_point.cave.abbr, str(self.sampling_point.point_number), self.host_type, self.sample_type])
        super(Source, self).save(*args, **kwargs)

    def __str__(self):
        return self.human_readable_id
    
class Strain(models.Model):
    source = models.ForeignKey(Source, related_name='strains', on_delete=models.CASCADE)
    human_readable_id = models.CharField(max_length=150, blank=True)
    accession_no = models.CharField(max_length=100, blank=True)
    type = models.IntegerField()    # 1 - Bacteria, 2 = Yeast, 3 = Mold
    type_id = models.IntegerField(blank=True)


    def save(self, *args, **kwargs):
        if not self.type_id:
            self.type_id = self.source.strains.count() + 1
        
        self.human_readable_id = '-'.join([self.source.human_readable_id, str(self.type_id).zfill(3)])
        self.accession_no = '-'.join([self.source.collection, self.source.institution, str((4 + self.type) * 10000 + self.type_id)])
        super(Strain, self).save(*args, **kwargs)

    def __str__(self):
        return self.human_readable_id