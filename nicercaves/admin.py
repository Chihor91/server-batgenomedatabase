from django.contrib import admin
from .models import (
	Article
)
from upload.models import ArticlePhoto

# Register your models here.
admin.site.register(Article)
admin.site.register(ArticlePhoto)