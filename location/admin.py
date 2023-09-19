from django.contrib import admin
from .models import (
    Location,
    Cave,
    SamplingPoint
)
# Register your models here.
admin.site.register(Location)
admin.site.register(Cave)
admin.site.register(SamplingPoint)