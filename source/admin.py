from django.contrib import admin
from .models import (
    Project,
    Source,
)
# Register your models here.
admin.site.register(Project)
admin.site.register(Source)