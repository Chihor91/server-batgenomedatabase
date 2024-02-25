from rest_framework.routers import DefaultRouter

from .views import (
    SourceViewSet,
    StrainViewSet,
)

router = DefaultRouter()

router.register('source', SourceViewSet)
router.register('isolate', StrainViewSet)

urlpatterns = router.urls