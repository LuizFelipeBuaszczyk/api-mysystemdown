from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema

from iam.permissions.systems_permissions import SystemPermission 
from systems.serializers.system_serializer import SystemReadSerializer, SystemWriteSerializer, SystemListReadSetializer
from systems.services.system_service import SystemService


# Create your views here.
@extend_schema_view(
    list=extend_schema(
        responses={200: SystemListReadSetializer}
    ),
    create=extend_schema(
        request=SystemWriteSerializer,
        responses={201: SystemReadSerializer},
    )
)
class SystemViewSet(GenericViewSet):
    permission_classes = [SystemPermission]
    
    def list(self, request):
        systems = SystemService.list_systems() 
        
        return Response(
            data=SystemListReadSetializer(systems).data,
            status=status.HTTP_200_OK
        )
    
    def create(self, request):
        serializer = SystemWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        system = SystemService.create_system(
            data=serializer.validated_data
        )
        
        return Response(
            SystemReadSerializer(system).data,
            status=status.HTTP_201_CREATED
        )