from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    TestView
)

# router = DefaultRouter()

urlpatterns = [
    path('test', TestView.as_view(), name="test")
]

# urlpatterns = router.urls