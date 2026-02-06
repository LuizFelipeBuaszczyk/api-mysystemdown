from rest_framework import serializers

class LoginResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh = serializers.CharField()
    
class LoginRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()