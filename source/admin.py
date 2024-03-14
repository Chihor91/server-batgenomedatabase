from django.contrib import admin
from .models import (
    Source,
    Isolate,
)
# Register your models here.
admin.site.register(Source)
admin.site.register(Isolate)