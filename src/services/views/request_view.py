from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from uuid import UUID

from iam.permissions.request_permissions import RequestPermission
from systems.models import Service 
from services.services.request_service import RequestService

from services.serializers.request_serializer import RequestListReadSerializer, RequestWriteSerializer, RequestReadSerializer

from utils.logger import get_logger

logger = get_logger(__name__)

@extend_schema_view(
    list=extend_schema(
        responses={200: RequestListReadSerializer},        
        parameters=[
            OpenApiParameter(
                name="service_pk", 
                type=UUID, 
                location=OpenApiParameter.PATH,
                description="Service primary key"
            )
        ]
        ),
    create=extend_schema(
        request=RequestWriteSerializer,
        responses={201: RequestReadSerializer},
        parameters=[
            OpenApiParameter(
                name="service_pk", 
                type=UUID, 
                location=OpenApiParameter.PATH,
                description="Service primary key"
            ),
            OpenApiParameter(
                name="api-token",
                type=str,
                required=True,
                location=OpenApiParameter.HEADER,
                description="API Token"
            )
        ]
    )
)
class RequestViewSet(GenericViewSet):
    permission_classes = [RequestPermission]
    
    def list(self, request, service_pk=None):
        logger.info(f"Listing requests - user_id: {request.user.id}, service_pk: {service_pk}")
        service = get_object_or_404(Service, id=service_pk)
        
        requests = RequestService.list_requests_by_service(service)
        
        return Response(
            data=RequestListReadSerializer(requests).data, 
            status=status.HTTP_200_OK
            )
        
    def create(self, request, service_pk=None):
        logger.info(f"Create request - user_id: {request.user.id}, service_pk: {service_pk}")
        service = get_object_or_404(Service, id=service_pk)
        
        serializer = RequestWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        request = RequestService.create_request(
            data=serializer.validated_data, 
            service=service
        )
        
        return Response(
            RequestReadSerializer(request).data, 
            status=status.HTTP_201_CREATED
        )
