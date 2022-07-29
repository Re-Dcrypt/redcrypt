# Generated by Django 4.0.4 on 2022-07-29 14:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hunt', '0006_samplequestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplequestion',
            name='completed_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]