from django.conf import settings
from django.db import models
from systems.models import System

# Create your models here.
class Membership(models.Model):
    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("admin", "Admin"),
        ("viewer", "Viewer"),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=False, blank=False, default="viewer")
    
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("user", "system")

    def __str__(self):
        return f"{self.user.email} → {self.system.name} ({self.role})"