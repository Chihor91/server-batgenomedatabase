from rest_framework import routers
from .views import IsolateViewSet

isolate_router = routers.DefaultRouter()

isolate_router.register('', IsolateViewSet)

urlpatterns = isolate_router.urls