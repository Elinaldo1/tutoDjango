# Generated by Django 4.2.3 on 2023-07-15 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_fleet_location_operation_statusfleet_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logagricola',
            name='name',
        ),
    ]