from django.db import models

# Create your models here.
class Isolate(models.Model):
    class Meta:
        verbose_name_plural = "isolates"

    isolate_name = models.CharField(max_length=20)
    def __str__(self):
        return self.isolate_name