from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UrlShortner(models.Model):
    active = models.BooleanField(default=True)
    short_url = models.CharField(max_length=150, unique=True)
    is_content = models.BooleanField(default=False)
    content = models.TextField(max_length=999999, blank=True, null=True)
    full_url = models.CharField(max_length=999999, blank=True, null=True)
    click_counts = models.IntegerField(default=0)
    visited_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return str(self.short_url)
