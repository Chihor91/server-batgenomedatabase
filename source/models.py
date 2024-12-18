from django.db import models
from user.models import Account
	# Create your models here.

class Source(models.Model):
	collection_name = models.CharField(max_length=512)
	collection = models.CharField(max_length=25)

	institution_name = models.CharField(max_length=512)
	institution = models.CharField(max_length=25)

	host_type = models.CharField(max_length=25, blank=True) 
	host_species = models.CharField(max_length=50, blank=True)
	sample_type = models.CharField(max_length=25)

	project_name = models.CharField(max_length=512)
	project_abbr = models.CharField(max_length=25)

	loc_province = models.CharField(max_length=50)
	loc_city = models.CharField(max_length=50)
	loc_abbr = models.CharField(max_length=25)
	loc_sampling_site = models.CharField(max_length=50)
	loc_site_abbr = models.CharField(max_length=25)
	loc_sampling_point = models.IntegerField(default=0)
	loc_longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
	loc_latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

	miso_categories = models.JSONField(blank=True, default=dict)
	miso_categories_string = models.CharField(max_length=1000, blank=True)

	raw_human_readable_id = models.CharField(max_length=150, blank=True)
	human_readable_id = models.CharField(max_length=150, blank=True)

	isolate_counter = models.IntegerField(default=0)

	author_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="sources")
	author = models.CharField(max_length=150)

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

class AccessionCounter(models.Model):
	raw_accession_no = models.CharField(max_length=100, blank=True)
	count = models.IntegerField(default=0)

class Isolate(models.Model):
	source = models.ForeignKey(Source, related_name='isolates', on_delete=models.CASCADE)
	human_readable_id = models.CharField(max_length=150, blank=True)

	accession_no = models.CharField(max_length=100, blank=True)
	type = models.IntegerField()    # 1 - Bacteria, 2 = Yeast, 3 = Mold

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

		self.source.isolate_counter += 1
		self.source.save()

		raw_accession_no = '-'.join([self.source.collection, self.source.institution, str((4 + self.type) * 10000)])
		
		try:
			accession_count = AccessionCounter.objects.get(raw_accession_no = raw_accession_no)
		except AccessionCounter.DoesNotExist:
			accession_count = AccessionCounter.objects.create(raw_accession_no = raw_accession_no)

		accession_count.count += 1
		accession_count.save()

		self.human_readable_id = '-'.join([self.source.human_readable_id, str(self.source.isolate_counter).zfill(3)])
		self.accession_no = '-'.join([self.source.collection, self.source.institution, str((4 + self.type) * 10000 + accession_count.count)])
		super(Isolate, self).save(*args, **kwargs)

	def __str__(self):
		return self.human_readable_id
	
