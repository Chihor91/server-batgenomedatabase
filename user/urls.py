from django.urls import path

from .views import LoginViewSet, IsLoggedIn, IsAdmin
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login/', LoginViewSet.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('isloggedin/', IsLoggedIn.as_view(), name='is logged in'),
    path('isadmin/', IsAdmin.as_view(), name='is admin')
]