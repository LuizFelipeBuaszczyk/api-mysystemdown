from rest_framework import serializers
from systems.models import System

class SystemReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = System
        fields = "__all__"
        
class SystemListReadSetializer(serializers.ListSerializer):
    child = SystemReadSerializer()

class SystemWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = System
        fields = ["name", "description"]
        