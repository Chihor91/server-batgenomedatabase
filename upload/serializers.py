from rest_framework import serializers
from .models import ArticlePhoto

class ArticlePhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticlePhoto
		fields = '__all__'