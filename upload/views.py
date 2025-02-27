from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import ArticlePhoto
from .serializers import ArticlePhotoSerializer
from nicercaves.models import Article

# Create your views here.
class ArticlePhotoViewSet(viewsets.ModelViewSet):
	parser_classes = [MultiPartParser, FormParser]
	queryset = ArticlePhoto.objects.all()
	serializer_class = ArticlePhotoSerializer

	def create(self, request, *args, **kwargs):
		user = request.user

		try:
			article = Article.objects.get(pk=request.data['article'])
			if user.is_superuser or user == article.author:
				return super().create(request, *args, **kwargs)
		except Exception as e:
			print(e)
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
	def destroy(self, request, pk=None, *args, **kwargs):
		user = request.user
		photo = get_object_or_404(self.get_queryset(), pk=pk)
		serializer = self.get_serializer(photo)
		article = get_object_or_404(Article, pk=serializer.data['article'])

		if (user.is_superuser or user.id == article.author):
			response = super().destroy(request, *args, **kwargs)
			return response
		else:
			return Response(
				{'error': 'Unauthorized'},
				status= status.HTTP_401_UNAUTHORIZED
			)
		
	@action(detail=False)
	def photos_from_article(self, request, *args, **kwargs):
		articleID = kwargs['article']
		images = ArticlePhoto.objects.filter(article=articleID)

		serializer = self.get_serializer(images, many=True)
		return Response(serializer.data)