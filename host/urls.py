from rest_framework import routers

from .views import HostViewSet

host_router = routers.DefaultRouter()

host_router.register('', HostViewSet)

urlpatterns = host_router.urls