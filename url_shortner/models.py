from django.db import models

# Create your models here.


class UrlShortner(models.Model):
    short_url = models.CharField(max_length=150)
    full_url = models.CharField(max_length=999999)
    click_counts = models.IntegerField(default=0)

    def __str__(self):
        return str(self.short_url)
