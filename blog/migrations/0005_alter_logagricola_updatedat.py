# Generated by Django 4.2.3 on 2023-07-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_logagricola_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logagricola',
            name='updatedAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
