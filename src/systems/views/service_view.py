from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from uuid import UUID

from iam.permissions.service_permissions import ServicePermission   
from systems.models import System, Service

from systems.serializers.service_serializer import SystemServiceReadSerializer, SystemServiceWriteSerializer
from systems.services.service_service import ServiceService

@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name="system_pk",
                type=UUID,
                location=OpenApiParameter.PATH,
                description="System's UUID"
            ),
        ]
    ),
    create=extend_schema(
        request=SystemServiceWriteSerializer,
        responses={201: SystemServiceReadSerializer},
        parameters=[
            OpenApiParameter(
                name="system_pk",
                type=UUID,
                location=OpenApiParameter.PATH,
                description="System's UUID"
            ),
        ]
    )
)
class ServiceViewSet(GenericViewSet):
    permission_classes = [ServicePermission]    
    
    ## Declara qual serializer será utilizado de acordo com a ação
    def get_serializer_class(self):
        if self.action == "create":
            return SystemServiceWriteSerializer
        return SystemServiceReadSerializer
    
    @extend_schema(
        parameters=[            
            OpenApiParameter(
                name="actives", 
                type=bool, 
                location=OpenApiParameter.QUERY,
                required=False,
                default=True,
                description="Filter just active services"
            ),
        ]
    )
    def list(self, request, system_pk: UUID):
        just_actives = request.query_params.get("actives", "false").lower() == "true"
        
        system = get_object_or_404(System, id=system_pk)
        services = ServiceService.list_services(system=system, just_actives=just_actives)
        
        return Response(
            data=SystemServiceReadSerializer(services, many=True).data,
            status=status.HTTP_200_OK
        )      

    def create(self, request, system_pk=None):
        system = get_object_or_404(System, id=system_pk)
        serializer = SystemServiceWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ServiceService.create_service(
            data=serializer.validated_data,
            system=system
        )
        
        return Response(
            SystemServiceReadSerializer(service).data,
            status=status.HTTP_201_CREATED
        )