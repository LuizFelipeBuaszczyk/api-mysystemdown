
from iam.models import Membership

from systems.models import System
from users.models import User

class MembershipRepository:
    
    @staticmethod
    def get_memberships_by_system(system: System):
        return Membership.objects.filter(system=system).select_related("user")
    
    @staticmethod
    def crate_membership(data: dict):
        return Membership.objects.create(**data)