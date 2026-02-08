from uuid import uuid4
from django.conf import settings
from django.db import models
from django.contrib.auth.models import Group
from tenants.models import Client

# Create your models here.
class Membership(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, 
        editable=False
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="memberships")
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="memberships")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="memberships")
    
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("user", "tenant")

    def __str__(self):
        return f"{self.user.email} → {self.tenant.name} ({self.group})"