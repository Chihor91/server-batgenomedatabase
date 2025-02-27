from django.urls import path, re_path
from .views import ArticleViewSet
from upload.views import ArticlePhotoViewSet

urlpatterns = [
	path('articles/', ArticleViewSet.as_view({'get': 'list'}), name='get articles'),
	path('article/add', ArticleViewSet.as_view({'post': 'create'}), name='create article'),
	path('article/id/<int:pk>/', ArticleViewSet.as_view({'get': 'retrieve'}), name='get article'),
	path('article/delete/<int:pk>/', ArticleViewSet.as_view({'delete': 'destroy'}), name='delete article'),
	path('article/edit/<int:pk>/', ArticleViewSet.as_view({'put': 'update'}), name='edit article'),
	path('article/images/add/', ArticlePhotoViewSet.as_view({'post': 'create'})),
	path('article/images/delete/<int:pk>/', ArticlePhotoViewSet.as_view({'delete': 'destroy'}), name='delete article photo'),
	re_path('article/images/(?P<article>.+)/$', ArticlePhotoViewSet.as_view({'get': 'photos_from_article'})),

]