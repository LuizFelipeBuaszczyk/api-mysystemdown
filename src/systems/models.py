from django.db import models
from django.core.validators import MinValueValidator
from uuid import uuid4

# Create your models here.    
class System(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, 
        editable=False
    )
    name = models.CharField(
        max_length=50, 
        null=False
    )
    description = models.TextField(
        blank=True, 
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Service(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, 
        editable=False
    )
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    url = models.URLField(
        blank=False, 
        max_length=200, 
        null=False
    )
    description = models.TextField(
        blank=True, 
        null=True
    )
    health_check_interval = models.PositiveIntegerField(
        default=60, 
        validators=[MinValueValidator(10)],
        help_text="Interval in minutes between health checks"
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Foreign Keys
    system = models.ForeignKey(
        System, 
        on_delete=models.CASCADE,
        related_name="services"
        )
    
    class Meta:
        indexes = [
            models.Index(fields=["system"]),
            models.Index(fields=["is_active"])
        ]
    
    def __str__(self) -> str:
        return self.url
    
class Bot(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, 
        editable=False
    )
    
    bot_name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    
    prefix_token = models.CharField(
        max_length=12,
        blank=False,
        null=False,
        default="bot_token_"
    )
    
    api_token = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    system = models.ForeignKey(
        System, 
        on_delete=models.CASCADE,
        related_name="bots"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)