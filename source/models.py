from django.db import models
from user.models import Account
# Create your models here.

class Source(models.Model):
    collection = models.CharField(max_length=25)
    institution = models.CharField(max_length=150)
    
    host_type = models.CharField(max_length=25, blank=True) 
    host_species = models.CharField(max_length=50, blank=True)
    sample_type = models.CharField(max_length=25)

    project_name = models.CharField(max_length=150)
    project_abbr = models.CharField(max_length=25)


    loc_location = models.CharField(max_length=50)
    loc_abbr = models.CharField(max_length=25)
    loc_sampling_site = models.CharField(max_length=50)
    loc_site_abbr = models.CharField(max_length=25)
    loc_sampling_point = models.IntegerField(default=0)

    raw_human_readable_id = models.CharField(max_length=150, blank=True)
    human_readable_id = models.CharField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if (self.host_type == ""):

            self.raw_human_readable_id = '-'.join([self.collection, self.institution, self.project_abbr, self.loc_abbr, self.loc_site_abbr, str(self.loc_sampling_point), self.sample_type])
            self.human_readable_id = '-'.join([self.raw_human_readable_id, str(Source.objects.filter(raw_human_readable_id=self.raw_human_readable_id).count())])
        else: 
            self.raw_human_readable_id = '-'.join([self.collection, self.institution, self.project_abbr, self.loc_abbr, self.loc_site_abbr, str(self.loc_sampling_point), self.host_type, self.sample_type])
            self.human_readable_id = '-'.join([self.raw_human_readable_id, str(Source.objects.filter(raw_human_readable_id=self.raw_human_readable_id).count())])
        super(Source, self).save(*args, **kwargs)

    def __str__(self):
        return self.human_readable_id
    
class Isolate(models.Model):
    source = models.ForeignKey(Source, related_name='isolates', on_delete=models.CASCADE)
    human_readable_id = models.CharField(max_length=150, blank=True)
    accession_no = models.CharField(max_length=100, blank=True)
    type = models.IntegerField()    # 1 - Bacteria, 2 = Yeast, 3 = Mold
    type_id = models.IntegerField(blank=True)

    # BACDIVE FIELDS
    description = models.CharField(max_length=1000, blank=True)
    
    taxonomy = models.JSONField(blank=True, default=dict)
    morphology = models.JSONField(blank=True, default=dict)
    culture_growth = models.JSONField(blank=True, default=dict)
    physiology_metabolism = models.JSONField(blank=True, default=dict)
    safety_information = models.JSONField(blank=True, default=dict)
    sequence_information = models.JSONField(blank=True, default=dict)

    visibility = models.CharField(max_length=20)
    author_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="isolates")
    author = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.type_id:
            self.type_id = self.source.isolates.count() + 1
        
        self.human_readable_id = '-'.join([self.source.human_readable_id, str(self.type_id).zfill(3)])
        self.accession_no = '-'.join([self.source.collection, self.source.institution, str((4 + self.type) * 10000 + self.type_id)])
        super(Isolate, self).save(*args, **kwargs)

    def __str__(self):
        return self.human_readable_id