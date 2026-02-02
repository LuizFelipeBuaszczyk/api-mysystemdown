from rest_framework import serializers
from iam.models import Membership
from users.serializers import UserReadSerializer
        
class MembershipReadSerializer(serializers.ModelSerializer):
    user = UserReadSerializer()
    
    class Meta:
        model = Membership
        fields = ["id", "role", "joined_at", "user"]
        
class MembershipListReadSerializer(serializers.ListSerializer):
    child = MembershipReadSerializer()
    
class MembershipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ["user", "role"]