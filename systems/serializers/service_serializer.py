from rest_framework import serializers
from systems.models import Service

class ServiceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class ServiceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["title", "url", "description", "health_check_interval"]