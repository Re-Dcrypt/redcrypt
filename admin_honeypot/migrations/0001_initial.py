# Generated by Django 4.1 on 2022-09-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='username')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip address')),
                ('session_key', models.CharField(blank=True, max_length=50, null=True, verbose_name='session key')),
                ('user_agent', models.TextField(blank=True, null=True, verbose_name='user-agent')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('path', models.TextField(blank=True, null=True, verbose_name='path')),
            ],
            options={
                'verbose_name': 'login attempt',
                'verbose_name_plural': 'login attempts',
                'ordering': ('timestamp',),
            },
        ),
    ]