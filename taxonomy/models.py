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
    parent = models.ForeignKey(Domain, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Class(models.Model):
    class Meta:
        verbose_name_plural = "Classes"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Phylum, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    class Meta:
        verbose_name_plural = "Orders"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Family(models.Model):
    class Meta:
        verbose_name_plural = "Families"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Genus(models.Model):
    class Meta:
        verbose_name_plural = "Genera"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Species(models.Model):
    class Meta:
        verbose_name_plural = "Species"

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Genus, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
# Children Models
class Domain_Child(models.Model):

    class Meta:
        verbose_name_plural = "Domain_Children"

    domain_parent = models.ForeignKey(Domain, on_delete=models.CASCADE)
    domain_child = models.ForeignKey(Phylum, on_delete=models.CASCADE)

    def __str__(self):
        return self.domain_parent.name

class Phylum_Child(models.Model):

    class Meta:
        verbose_name_plural = "Phylum_Children"

    phylum_parent = models.ForeignKey(Phylum, on_delete=models.CASCADE)
    phylum_child = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.phylum_parent.name


class Class_Child(models.Model):

    class Meta:
        verbose_name_plural = "Class_Children"

    class_parent = models.ForeignKey(Class, on_delete=models.CASCADE)
    class_child = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_parent.name

class Order_Child(models.Model):

    class Meta:
        verbose_name_plural = "Order_Children"

    order_parent = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_child = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_parent.name

class Family_Child(models.Model):

    class Meta:
        verbose_name_plural = "Family_Children"

    family_parent = models.ForeignKey(Family, on_delete=models.CASCADE)
    family_child = models.ForeignKey(Genus, on_delete=models.CASCADE)

    def __str__(self):
        return self.family_parent.name

class Genus_Child(models.Model):

    class Meta:
        verbose_name_plural = "Genus_Children"

    genus_parent = models.ForeignKey(Genus, on_delete=models.CASCADE)
    genus_child = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return self.genus_parent.name

class Species_Child(models.Model):

    class Meta:
        verbose_name_plural = "Species_Children"

    species_parent = models.ForeignKey(Species, on_delete=models.CASCADE)
    # species_child = models.ForeignKey("", on_delete=models.CASCADE)

    def __str__(self):
        return self.species_parent.name
