from .models import Account
from .serializers import AccountSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class LoginViewSet(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        user = Account.objects.get(username=request.data.get('username'))

        serializer.validated_data['user'] = AccountSerializer(user).data

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
class IsLoggedIn(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

class IsAdmin(APIView):
    permission_classes = [IsSuperUser]

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

