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

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "User Progress"
