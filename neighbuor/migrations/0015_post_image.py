# Generated by Django 3.2.5 on 2021-07-25 21:00

import cloudinary.models
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighbuor', '0014_auto_20210725_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]