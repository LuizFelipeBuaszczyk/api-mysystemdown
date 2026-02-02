from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from systems.models import System
from iam.services.membership_service import MembershipService
from iam.serializers.membership_serializer import MembershipReadSerializer, MembershipListReadSerializer


class MembershipViewSet(ViewSet):
    permission_classes = [IsAuthenticated]       

    def get(self, request, system_pk=None):
        system = get_object_or_404(System, id=system_pk)
        memberships = MembershipService.get_membership_by_system(system)  
        print(memberships)
        
        serializer = MembershipListReadSerializer(memberships)
        return Response(serializer.data, status=200)

    def create(self, request, system_pk=None):
        system = get_object_or_404(System, id=system_pk)

        membership = MembershipService.create_membership(
            data=request.data,
            system=system,
            user=request.user
        )

        serializer = MembershipReadSerializer(membership)
        return Response(serializer.data, status=201)
