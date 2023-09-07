from django.contrib import admin
from .models import (
    Location,
    SamplingSite,
    SamplingPoint
)
# Register your models here.
admin.site.register(Location)
admin.site.register(SamplingSite)
admin.site.register(SamplingPoint)