
from iam.models import Membership

from tenants.models import Client
from users.models import User

class MembershipRepository:
    
    @staticmethod
    def get_memberships_by_tenant(tenant: Client):
        return Membership.objects.filter(tenant=tenant).select_related("user")
    
    @staticmethod
    def crate_membership(data: dict):
        return Membership.objects.create(**data)