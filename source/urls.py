from rest_framework.routers import DefaultRouter

from .views import (
    SourceViewSet,
    IsolateViewSet,
    ProjectViewSet
)

router = DefaultRouter()

router.register('source', SourceViewSet)
router.register('isolate', IsolateViewSet)
router.register('project', ProjectViewSet)

urlpatterns = router.urls