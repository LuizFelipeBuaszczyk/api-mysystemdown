from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from iam.serializers.token_serializer import RefreshTokenRequestSerializer, RefreshTokenResponseSerializer
from iam.services.auth_service import AuthService

class RefreshTokenView(APIView):
   
   @extend_schema(
       request=RefreshTokenRequestSerializer,
       responses={
           200: RefreshTokenResponseSerializer
       }
   )
   def post(self, request):
        serializer = RefreshTokenRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = AuthService.refresh_token(
            data=serializer.validated_data
        )

        return Response(result, status=status.HTTP_200_OK)