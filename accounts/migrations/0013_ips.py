# Generated by Django 4.0.4 on 2022-05-30 06:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0012_alter_profile_ip_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=150)),
                ('count', models.IntegerField(default=0)),
                ('users_from_ip', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
