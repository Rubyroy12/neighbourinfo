# Generated by Django 3.2.5 on 2021-07-25 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbuor', '0010_alter_location_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='neighbuor.profile'),
        ),
    ]
