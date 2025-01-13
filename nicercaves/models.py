from django.db import models
from django.utils import timezone
from user.models import Account

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.CharField(max_length=150)
	author_id = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="articles")
	photos = models.JSONField(blank=True, default=dict)
	date_created = models.DateTimeField(default=timezone.now)