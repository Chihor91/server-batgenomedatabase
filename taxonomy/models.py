from django.db import models

# Create your models here.
class Domain(models.Model):
    class Meta:
        verbose_name_plural = "Domain"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Phylum(models.Model):
    class Meta:
        verbose_name_plural = "Phyla"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Domain, related_name='phyla',  on_delete=models.CASCADE)
    
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