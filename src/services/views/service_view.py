from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter

from uuid import UUID

from systems.models import Service
from iam.permissions.service_permissions import ServicePermission
from services.services.service_service import ServiceService
from services.serializers.service_serializer import ServiceReadSerializer, ServiceDeleteSerializer

@extend_schema_view(
    retrieve=extend_schema(
        responses={200: ServiceReadSerializer},
    ),
    destroy=extend_schema(
        responses={200: ServiceDeleteSerializer}
    )
)
class ServiceViewSet(GenericViewSet):
    permission_classes = [ServicePermission]
    
    def get_queryset(self):
        return Service.objects.filter(id = self.kwargs.get('pk'))
    
    def retrieve(self, request, pk: UUID):
        service = self.get_object() 
        
        return Response(
            ServiceReadSerializer(service).data, 
            status=200
        )
    
    def destroy(self, request, pk: UUID):
        service = self.get_object()
        ServiceService.destroy_service(service)
        
        serializer = ServiceDeleteSerializer({
            "message": "Service deleted successfully",
            "deleted_id": pk
        })
        
        return Response(
            serializer.data,
            status=200
        )