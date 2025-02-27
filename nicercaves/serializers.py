from rest_framework import serializers

from .models import (
	Article
)
from upload.models import ArticlePhoto

class PhotoSerializer(serializers.ModelSerializer):

	class Meta:
		model = ArticlePhoto
		fields = ('id', 'article', 'photo')
	
class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ('id', 'title', 'content', 'author_name', 'date_created', 'author')

class ViewArticleSerializer(serializers.ModelSerializer):
	photos = PhotoSerializer(many=True)
	class Meta:
		model = Article
		fields = ('id', 'title', 'content', 'author_name', 'date_created', 'author', 'photos')
