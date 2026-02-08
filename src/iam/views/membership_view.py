from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema

from iam.permissions.membership_permissions import MembershipPermission
from iam.services.membership_service import MembershipService
from iam.serializers.membership_serializer import MembershipReadSerializer, MembershipListReadSerializer, MembershipCreateSerializer


@extend_schema_view(
    list=extend_schema(
        responses={200: MembershipListReadSerializer}
    ),
    create=extend_schema(
        request=MembershipCreateSerializer,
        responses={201: MembershipReadSerializer}
    )
)
class MembershipViewSet(GenericViewSet):
    permission_classes = [MembershipPermission]       

    def list(self, request):
        tenant = request.tenant
        memberships = MembershipService.get_membership_by_tenant(tenant)  
        
        serializer = MembershipListReadSerializer(memberships)
        return Response(serializer.data, status=200)

    def create(self, request):
        tenant = request.tenant
        serializer = MembershipCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        data["tenant"] = tenant

        membership = MembershipService.create_membership(
            data=data
        )

        serializer = MembershipReadSerializer(membership)
        return Response(serializer.data, status=201)
