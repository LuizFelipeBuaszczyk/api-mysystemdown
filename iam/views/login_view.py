from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from iam.services.auth_service import AuthService

# Create your views here.

class LoginView(APIView):
    
    def post(self, request):
        data = request.data
        result = AuthService.login(
            email=data.get("email"),
            password=data.get("password")
        )
        return Response(
            result,
            status=status.HTTP_200_OK
            )
        