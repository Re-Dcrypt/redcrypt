# Generated by Django 4.0.7 on 2022-09-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_completed_time',
            field=models.DateTimeField(),
        ),
    ]
