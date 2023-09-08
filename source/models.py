from django.db import models

# Create your models here.

class Source(models.Model):
    source_collection = models.CharField(max_length=255)
    source_institution = models.CharField(max_length=255)
    source_project = models.CharField(max_length=255)
    type_id = models.IntegerField(blank=True)
    accession_no = models.CharField(max_length=255, blank=True)

class Bacteria(Source):
    bacteria_id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        super(Bacteria, self).save(*args, **kwargs)
        self.type_id = self.bacteria_id + 50000
        self.accession_no = self.source_collection + '-' + self.source_institution + '-' + self.type_id
        super(Bacteria, self).save(*args, **kwargs)

class Yeast(Source):
    yeast_id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        super(Yeast, self).save(*args, **kwargs)
        self.type_id = self.yeast_id + 60000
        self.accession_no = self.source_collection + '-' + self.source_institution + '-' + self.type_id
        super(Yeast, self).save(*args, **kwargs)

class Mold(Source):
    mold_id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        super(Mold, self).save(*args, **kwargs)
        self.type_id = self.mold_id + 70000
        self.accession_no = self.source_collection + '-' + self.source_institution + '-' + self.type_id
        super(Mold, self).save(*args, **kwargs)
