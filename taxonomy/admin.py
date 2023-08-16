from django.contrib import admin
from . import models


admin.site.register(models.Domain)
admin.site.register(models.Phylum)
admin.site.register(models.Class)
admin.site.register(models.Order)
admin.site.register(models.Family)
admin.site.register(models.Genus)
admin.site.register(models.Species)