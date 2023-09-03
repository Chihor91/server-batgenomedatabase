from django.db import models

# Create your models here.
class Taxonomy(models.Model):
    class Meta:
        verbose_name_plural = "Taxonomic Classifications"
    
    tax_domain = models.CharField(max_length=100)
    tax_kingdom = models.CharField(max_length=100)
    tax_phylum = models.CharField(max_length=100)
    tax_class = models.CharField(max_length=100)
    tax_order = models.CharField(max_length=100)
    tax_family = models.CharField(max_length=100)
    tax_genus = models.CharField(max_length=100)
    tax_species = models.CharField(max_length=100)

    def __str__(self):
        return self.tax_species

class Strain(models.Model):
    class Meta:
        verbose_name_plural = "Strains"

    designation = models.CharField()
    taxonomy = models.ForeignKey(Taxonomy, related_name='strains', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.taxonomy.tax_species