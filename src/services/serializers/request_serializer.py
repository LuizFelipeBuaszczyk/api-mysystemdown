from rest_framework import serializers

from services.models import Request


class RequestWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ["status_code", "response_body", "response_headers", "response_time_ms"]

class RequestReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ["id", "status_code", "response_time_ms", "response_size_bytes"]
        

class RequestListReadSerializer(serializers.ListSerializer):
    child = RequestReadSerializer()