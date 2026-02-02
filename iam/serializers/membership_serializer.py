from rest_framework import serializers
from iam.models import Membership
from users.serializers import UserReadSerializer
from systems.serializers import SystemReadSerializer
        
class MembershipReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer()
    
    class Meta:
        model = Membership
        fields = ["id", "role", "joined_at", "user"]
        
class MembershipListReadSerializer(serializers.ListSerializer):
    child = MembershipReadSerializer()