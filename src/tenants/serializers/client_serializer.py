from rest_framework import serializers
from tenants.models import Client

class ClientWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["schema_name", "name"]

class ClientReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "schema_name", "name"]