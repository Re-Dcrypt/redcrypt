# Generated by Django 4.1 on 2022-09-01 17:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShortner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=150, unique=True)),
                ('is_content', models.BooleanField(default=False)),
                ('content', models.CharField(blank=True, max_length=999999, null=True)),
                ('full_url', models.CharField(blank=True, max_length=999999, null=True)),
                ('click_counts', models.IntegerField(default=0)),
                ('visited_by', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]