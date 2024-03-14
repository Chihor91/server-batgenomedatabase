from rest_framework.routers import DefaultRouter

from .views import (
    SourceViewSet,
    IsolateViewSet
)

router = DefaultRouter()

router.register('source', SourceViewSet)
router.register('isolate', IsolateViewSet)

urlpatterns = router.urls