from django.contrib import admin
from .models import (
    Source,
    Strain,
)
# Register your models here.
admin.site.register(Source)
admin.site.register(Strain)