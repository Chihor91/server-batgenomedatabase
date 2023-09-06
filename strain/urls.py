from rest_framework import routers
from django.urls import path
from .views import StrainViewSet

strain_router = routers.DefaultRouter()

strain_router.register('', StrainViewSet)

urlpatterns = strain_router.urls