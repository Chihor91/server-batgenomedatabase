from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.
from .serializers import (
	ArticleSerializer,
	ViewArticleSerializer
)

from .models import (
	Article
)

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	def get_serializer_class(self):
		if self.action in ['list', 'retrieve']:
			return ViewArticleSerializer
		return ArticleSerializer

	def retrieve(self, request, pk=None):
		article = get_object_or_404(self.get_queryset(), pk=pk)
		serializer = self.get_serializer(article)
        
		return Response(serializer.data)
	
	def destroy(self, request, pk=None, *args, **kwargs):
		user = request.user
		article = get_object_or_404(self.get_queryset(), pk=pk)
		serializer = self.get_serializer(article)

		if (user.is_superuser or user.id == serializer.data['author_id']):
			response = super().destroy(request, *args, **kwargs)

			return response
		else:
			return Response(
				{'error': 'Unauthorized'},
				status= status.HTTP_401_UNAUTHORIZED
			)
	
	def update(self, request, pk=None, *args, **kwargs):
		user = request.user
		article = get_object_or_404(self.get_queryset(), pk=pk)
		serializer = self.get_serializer(article)

		if (user.is_superuser or user.id == serializer.data['author_id']):
			response = super().update(request, *args, **kwargs)

			return response
		else:
			return Response(
				{'error': 'Unauthorized'},
				status= status.HTTP_401_UNAUTHORIZED
			)
	