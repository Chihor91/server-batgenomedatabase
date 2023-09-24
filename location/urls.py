from rest_framework.routers import DefaultRouter

from .views import (
    LocationViewSet,
    CaveViewSet,
    SamplingPointViewSet
)

router = DefaultRouter()

router.register('location', LocationViewSet)
router.register('cave', CaveViewSet)
router.register('point', SamplingPointViewSet)

urlpatterns = router.urls