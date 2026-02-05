from django.db import models
from uuid import uuid4

from systems.models import Service

# Create your models here.
class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status_code = models.PositiveSmallIntegerField(null=False, blank=False)
    response_body = models.JSONField(null=True, blank=True)
    response_headers = models.JSONField(null=True, blank=True)
    response_time_ms = models.PositiveIntegerField(null=False, blank=False)
    response_size_bytes = models.PositiveIntegerField(null=False, blank=False)
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)