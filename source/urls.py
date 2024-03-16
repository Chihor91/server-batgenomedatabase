from rest_framework.routers import DefaultRouter
from django.urls import path, re_path
from .views import (
    SourceViewSet,
    IsolateViewSet
)

router = DefaultRouter()

router.register('source', SourceViewSet)
router.register('isolate', IsolateViewSet)

urlpatterns = [
    path('view/all/', SourceViewSet.as_view({'get': 'list'})),
    path('view/id/<int:pk>/', SourceViewSet.as_view({'get': 'retrieve'})),
    path('add/', SourceViewSet.as_view({'post': 'create'})),

    path('isolate/view/all/', IsolateViewSet.as_view({'get': 'list'})),
    path('isolate/view/id/<int:pk>/', IsolateViewSet.as_view({'get': 'retrieve'})),
    path('isolate/source/<int:pk>/', IsolateViewSet.as_view({'get': 'get_by_id'})),
    path('isolate/add/', IsolateViewSet.as_view({'post': 'create'})),

]