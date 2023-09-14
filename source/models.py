from django.db import models
from host.models import Sample

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_abbr = models.CharField(max_length=50)

    def __str__(self):
        return self.project_abbr



class Source(models.Model):
    source_collection = models.CharField(max_length=255)
    source_institution = models.CharField(max_length=255)
    source_project = models.ForeignKey(Project, related_name='sources', on_delete=models.CASCADE)
    source_sample = models.ForeignKey(Sample, related_name="sources", on_delete=models.CASCADE)
    type_id = models.IntegerField(blank=True, default=0)
    accession_no = models.CharField(max_length=255, blank=True)
    source_id_human_readable = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.accession_no

class Bacteria(Source):
    sub_id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        super(Bacteria, self).save(*args, **kwargs)
        self.type_id = self.sub_id + 50000
        self.accession_no = self.source_collection + '-' + self.source_institution + '-' + str(self.type_id)
        self.source_id_human_readable = self.source_collection + '-' + self.source_institution + '-' + self.source_project.project_abbr + '-1-' + self.source_sample.sample_host.host_type + "-" + self.source_sample.sample_type
        super(Bacteria, self).save(*args, **kwargs)

    def __str__(self):
        return self.accession_no

class Yeast(Source):
    sub_id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        super(Yeast, self).save(*args, **kwargs)
        self.type_id = self.sub_id + 60000
        self.accession_no = self.source_collection + '-' + self.source_institution + '-' + str(self.type_id)
        super(Yeast, self).save(*args, **kwargs)

    def __str__(self):
        return self.accession_no

class Mold(Source):
    sub_id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        super(Mold, self).save(*args, **kwargs)
        self.type_id = self.sub_id + 70000
        self.accession_no = self.source_collection + '-' + self.source_institution + '-' + str(self.type_id)
        super(Mold, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.accession_no