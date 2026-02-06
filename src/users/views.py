from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema

from users.serializers import UserReadSerializer, UserWriteSerializer
from users.services.user_service import UserService

# Create your views here.
@extend_schema_view(
    create=extend_schema(
        request=UserWriteSerializer,
        responses={201: UserReadSerializer},
    )
)
class UserViewSet(GenericViewSet):
    
    def create(self, request):
        serializer = UserWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = UserService.create_user(serializer.validated_data)
        
        return Response(
            UserReadSerializer(user).data,
            status=status.HTTP_201_CREATED
        )