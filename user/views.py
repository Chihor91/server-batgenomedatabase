# from .models import Account
# from .serializers import AccountSerializer
# from django.http import JsonResponse
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# # Create your views here.
# class LogInViewSet(TokenObtainPairView):

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)

#         try:
#             serializer.is_valid(raise_exception=True)
#         except TokenError as e:
#             raise InvalidToken(e.args[0])
        
#         user = Account.objects.