# Generated by Django 3.2.5 on 2021-07-25 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbuor', '0005_auto_20210725_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='neighbuor.profile'),
        ),
    ]
