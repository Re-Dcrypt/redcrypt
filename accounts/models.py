"Django Models"
from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
import requests
import os
from dotenv import load_dotenv
load_dotenv()


class Profile(models.Model):
    "User model extended with more fields"
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    score = models.IntegerField(default=0)
    last_completed_time = models.DateTimeField(auto_now=True)
    is_public_name = models.BooleanField(default=False)
    current_level = models.IntegerField(default=0)
    discord_id = models.IntegerField(default=0)
    organization = models.CharField(max_length=150, blank=True)
    is_public_organization = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    banned_reason = models.CharField(max_length=150, blank=True)
    ip_address = models.JSONField(default=list)
    ip_address_count = models.IntegerField(default=0)
    avatar_url = models.CharField(
        max_length=150,
        default="https://avatars.dicebear.com/api/pixel-art-neutral/helooooooooooo.svg"
    )

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


class contact_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    body = models.TextField()


@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    profile = Profile.objects.get(user=user)
    "Send  discord webhook after user signup"
    name = profile.name if profile.name else "None"
    organization = profile.organization if profile.organization else "None"
    json_data = {"content": "New Signup", "embeds": [{
        "title": "New User Signup", "color": 53970, "fields": [
            {
                "name": "Username",
                "value": str(user.username)
            },
            {
                "name": "Name",
                "value": name
            },
            {
                "name": "Email",
                "value": str(user.email)
            },
            {
                "name": "School/Organisation",
                "value": organization
            }]}]}
    url = os.getenv("DISCORD_LOGGING_WEBHOOK")
    requests.post(url, json=json_data)
