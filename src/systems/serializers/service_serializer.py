from rest_framework import serializers
from systems.models import Service

class SystemServiceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title", "url", "description", "health_check_interval", "is_active"]

class SystemServiceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["title", "url", "description", "health_check_interval"]