from rest_framework import routers
from django.urls import path
from .views import (
    DomainViewSet,
    KingdomViewSet, 
    PhylumViewSet,
    ClassViewSet,
    OrderViewSet,
    FamilyViewSet,
    GenusViewSet,
    SpeciesViewSet
    )

tax_router = routers.DefaultRouter()

tax_router.register('domain', DomainViewSet)
tax_router.register('kingdom', KingdomViewSet)
tax_router.register('phylum', PhylumViewSet)
tax_router.register('class', ClassViewSet)
tax_router.register('order', OrderViewSet)
tax_router.register('family', FamilyViewSet)
tax_router.register('genus', GenusViewSet)
tax_router.register('species', SpeciesViewSet)

urlpatterns = tax_router.urls