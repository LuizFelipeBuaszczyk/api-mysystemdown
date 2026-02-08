from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema, extend_schema_view

from tenants.serializers.tenant_serializer import TenantWriteSerializer, TenantReadSerializer
from tenants.service.tenant_service import TenantService

# Create your views here.

@extend_schema_view(
    create=extend_schema(
        request=TenantWriteSerializer,
        responses={201: TenantReadSerializer}
    )
)
class TeanantView(GenericViewSet):
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        serializer = TenantWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        tenant = TenantService.create_tenant(serializer.validated_data, request.user)
        
        return Response(
            TenantReadSerializer(tenant).data,
            status=status.HTTP_201_CREATED
        )