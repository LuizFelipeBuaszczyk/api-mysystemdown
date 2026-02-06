from rest_framework import serializers

class RefreshTokenRequestSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
class RefreshTokenResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh = serializers.CharField()
