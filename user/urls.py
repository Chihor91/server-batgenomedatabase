from django.urls import path

from .views import LoginViewSet, IsLoggedIn, IsAdmin, AccountViewSet, LogViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('accounts/', AccountViewSet.as_view({'get': 'list'}), name='get accounts'),
    path('account/', AccountViewSet.as_view({'post': 'create'}), name='create account'),
    path('login/', LoginViewSet.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('isloggedin/', IsLoggedIn.as_view(), name='is logged in'),
    path('isadmin/', IsAdmin.as_view(), name='is admin'),
    path('logs/', LogViewSet.as_view({'get': 'list'})),

]