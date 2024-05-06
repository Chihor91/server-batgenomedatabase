from .models import Account, Log
from .serializers import AccountSerializer, LogSerializer
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

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
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def create(self, request):
        try:
            if request.user.is_superuser:
                data = request.data

                email = data['email']
                username = data['username']
                password = data['password']

                if Account.objects.filter(email = email).exists():
                    return Response(
                        {'error': 'Account with this email already exists.'},
                        status = status.HTTP_400_BAD_REQUEST
                    )
                elif Account.objects.filter(username = username).exists():
                    return Response(
                        {'error': 'Account with this username already exists.'},
                        status = status.HTTP_400_BAD_REQUEST
                    )
                else:
                    Account.objects.create_user(email = email, username = username, password = password)
                    Log.objects.create(type="User", detail="Created account " + username, userid=request.user, user=request.user.username)
                    return Response(
                        {'data': 'Account created successfully'},
                        status = status.HTTP_201_CREATED
                    )
            else:
                return Response(
                    {'error': 'Unauthorized'},
                    status = status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong while creating user.'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def list(self, request):
        user = request.user
        if user.is_superuser:
            serializer = self.get_serializer(Log.objects.all(), many=True)
            return Response(serializer.data)
        else:
            return Response(
                {'error': 'Unauthorized'},
                status=status.HTTP_401_UNAUTHORIZED
            )