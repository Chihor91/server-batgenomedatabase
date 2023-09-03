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
    scientific_name = str(tax_genus) + " " + str(tax_species).lower()

    def __str__(self):
        return self.tax_species


class Domain(models.Model):
    class Meta:
        verbose_name_plural = "Domain"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Kingdom(models.Model):
    class Meta:
        verbose_name_plural = "Kingdoms"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Domain, related_name='kingdoms',  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 

class Phylum(models.Model):
    class Meta:
        verbose_name_plural = "Phyla"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Kingdom, related_name='phyla',  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Class(models.Model):
    class Meta:
        verbose_name_plural = "Classes"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Phylum, related_name='classes',  on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    class Meta:
        verbose_name_plural = "Orders"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Class, related_name='orders',  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Family(models.Model):
    class Meta:
        verbose_name_plural = "Families"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Order, related_name='families',  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Genus(models.Model):
    class Meta:
        verbose_name_plural = "Genera"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Class, related_name='genera',  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Species(models.Model):
    class Meta:
        verbose_name_plural = "Species"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Genus, related_name='species', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name