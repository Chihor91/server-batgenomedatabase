from django.contrib import admin
from .models import (
    Project,
    Source,
    Isolate,
)
# Register your models here.
admin.site.register(Project)
admin.site.register(Source)
admin.site.register(Isolate)