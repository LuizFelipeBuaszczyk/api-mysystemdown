from rest_framework import serializers

class ConfirmRequestSerializer(serializers.Serializer):
    token = serializers.CharField()

class ConfirmResponseSerializer(serializers.Serializer):
    message = serializers.CharField()