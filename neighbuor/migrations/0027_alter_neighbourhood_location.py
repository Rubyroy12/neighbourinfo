# Generated by Django 3.2.5 on 2021-07-26 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbuor', '0026_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbuor.location'),
        ),
    ]