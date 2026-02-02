from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from systems.models import System

from systems.serializers.service_serializer import ServiceReadSerializer, ServiceWriteSerializer
from systems.services.service_service import ServiceService

@extend_schema_view(
    create=extend_schema(
        request=ServiceWriteSerializer,
        responses={201: ServiceReadSerializer},
        parameters=[
            OpenApiParameter(
                name="system_pk",
                type=str,
                location=OpenApiParameter.PATH,
                description="System's UUID"
            )
        ]
    )
)
class ServiceViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]    
    

    def create(self, request, system_pk=None):
        system = get_object_or_404(System, id=system_pk)
        serializer = ServiceWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ServiceService.create_service(
            data=serializer.validated_data,
            system=system
        )
        
        return Response(
            ServiceReadSerializer(service).data,
            status=status.HTTP_201_CREATED
        )