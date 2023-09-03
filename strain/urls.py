from rest_framework import routers

from .views import (
    TaxonomyViewSet,
    StrainViewSet
)

strain_router = routers.DefaultRouter()

strain_router.register('taxonomy', TaxonomyViewSet)
strain_router.register('strain', StrainViewSet)

urlpatterns = strain_router.urls