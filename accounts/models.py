"Django Models"
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    "User model extended with more fields"
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    score = models.IntegerField(default=0)
    is_public_name = models.BooleanField(default=False)
    current_level = models.IntegerField(default=0)
    discord_id = models.IntegerField(default=0)
    organization = models.CharField(max_length=150, blank=True)
    is_public_organization = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    banned_reason = models.CharField(max_length=150, blank=True)
    ip_address = models.JSONField(default=[""])

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "User Profiles"

class IPs(models.Model):
    "IP address model for catching cheaters"
    ip_address = models.CharField(max_length=150)
    users_from_ip = models.ManyToManyField(User)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.ip_address)

    class Meta:
        verbose_name_plural = "IP addresses"
