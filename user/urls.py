from django.urls import path

from .views import LoginViewSet, IsLoggedIn, IsAdmin, AccountViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('account/', AccountViewSet.as_view({'get': 'list', 'post': 'create'}), name='account'),
    path('login/', LoginViewSet.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('isloggedin/', IsLoggedIn.as_view(), name='is logged in'),
    path('isadmin/', IsAdmin.as_view(), name='is admin')
]