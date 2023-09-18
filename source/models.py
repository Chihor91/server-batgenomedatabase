from django.db import models
from host.models import Sample

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=25)

    def __str__(self):
        return self.abbr



class Source(models.Model):
    collection = models.CharField(max_length=25)
    institution = models.CharField(max_length=50)
    type = models.IntegerField()
    type_id = models.IntegerField(blank=True)
    accession_no = models.CharField(max_length=255, blank=True)
    human_readable_id = models.CharField(max_length=255, blank=True)

    project = models.ForeignKey(Project, related_name='sources', on_delete=models.CASCADE, blank=True)
    sample = models.ForeignKey(Sample, related_name='sources', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.type_id = (self.type + 4) * 10000 + (Source.objects.filter(type=self.type).count() + 1)
        self.accession_no = '-'.join([self.collection, self.institution, str(self.type_id)]) 
        self.human_readable_id = '-'.join([self.collection, self.institution, self.project.abbr, str(self.type), self.sample.host.type, self.sample.type])
        super(Source, self).save(*args, **kwargs)

    def __str__(self):
        return self.accession_no

# class Bacteria(Source):
#     sub_id = models.AutoField(primary_key=True)

#     def save(self, *args, **kwargs):
#         super(Bacteria, self).save(*args, **kwargs)
#         self.type_id = self.sub_id + 50000
#         self.accession_no = self.source_collection + '-' + self.source_institution + '-' + str(self.type_id)
#         self.source_id_human_readable = self.source_collection + '-' + self.source_institution + '-' + self.source_project.project_abbr + '-1-' + self.source_sample.sample_host.host_type + "-" + self.source_sample.sample_type
#         super(Bacteria, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.accession_no

# class Yeast(Source):
#     sub_id = models.AutoField(primary_key=True)

#     def save(self, *args, **kwargs):
#         super(Yeast, self).save(*args, **kwargs)
#         self.type_id = self.sub_id + 60000
#         self.accession_no = self.source_collection + '-' + self.source_institution + '-' + str(self.type_id)
#         self.source_id_human_readable = self.source_collection + '-' + self.source_institution + '-' + self.source_project.project_abbr + '-2-' + self.source_sample.sample_host.host_type + "-" + self.source_sample.sample_type
#         super(Yeast, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.accession_no

# class Mold(Source):
#     sub_id = models.AutoField(primary_key=True)

#     def save(self, *args, **kwargs):
#         super(Mold, self).save(*args, **kwargs)
#         self.type_id = self.sub_id + 70000
#         self.accession_no = self.source_collection + '-' + self.source_institution + '-' + str(self.type_id)
#         self.source_id_human_readable = self.source_collection + '-' + self.source_institution + '-' + self.source_project.project_abbr + '-3-' + self.source_sample.sample_host.host_type + "-" + self.source_sample.sample_type
#         super(Mold, self).save(*args, **kwargs)
    
#     def __str__(self):
#         return self.accession_no