from django.contrib import admin
from .models import (
    Host,
    Sample
)
# Register your models here.

admin.site.register(Host)
admin.site.register(Sample)