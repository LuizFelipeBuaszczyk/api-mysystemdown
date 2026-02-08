from rest_framework import serializers
from tenants.models import Domain

class DomainWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["domain"]


class DomainReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["id", "domain"]