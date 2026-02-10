from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema

from users.serializers import UserReadSerializer, UserWriteSerializer
from users.services.user_service import UserService

from utils.logger import get_logger

logger = get_logger(__name__)

# Create your views here.
@extend_schema_view(
    create=extend_schema(
        request=UserWriteSerializer,
        responses={201: UserReadSerializer},
    )
)
class UserViewSet(GenericViewSet):
    
    def create(self, request):
        logger.info(f"Create user")
        serializer = UserWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = UserService.create_user(serializer.validated_data)
        
        logger.info("User created")
        return Response(
            UserReadSerializer(user).data,
            status=status.HTTP_201_CREATED
        )