# Generated by Django 3.2.5 on 2021-07-26 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbuor', '0023_auto_20210726_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='neighbour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='neighbuor.neighbourhood'),
        ),
    ]