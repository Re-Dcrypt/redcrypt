# Generated by Django 4.0.4 on 2022-08-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_profile_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='stats',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]