from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    "User model extended with more fields"
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    current_level = models.IntegerField(default=0)
    discord_id = models.IntegerField(default=0)
    organization = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return str(self.user)
