# Generated by Django 4.2.7 on 2024-02-16 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='base_distance_in_km',
            field=models.IntegerField(),
        ),
    ]