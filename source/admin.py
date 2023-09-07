from django.contrib import admin
from .models import (
    Source,
    Bacteria,
    Yeast,
    Mold
)
# Register your models here.
admin.site.register(Source)
admin.site.register(Bacteria)
admin.site.register(Yeast)
admin.site.register(Mold)