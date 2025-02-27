import os
from django.db import models
from django.db.models.signals import pre_delete
from nicercaves.models import Article
from django.dispatch import receiver

def get_upload_path(instance, filename):
	return 'images/article/%d/%s' % (instance.article.id, filename)

# Create your models here.
class ArticlePhoto(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="photos")
	photo = models.ImageField(upload_to=get_upload_path)

@receiver(pre_delete, sender=ArticlePhoto, dispatch_uid='article photo delete')
def delete_image(sender, instance, using, **kwargs):
	instance.photo.delete(save=False)

@receiver(pre_delete, sender=Article, dispatch_uid='article delete')
def delete_image_dir(sender, instance, using, **kwargs):
	dirpath = os.path.join('images/article/', str(instance.id))
	if os.path.exists(dirpath) and os.path.isdir(dirpath):
		os.rmdir(dirpath)