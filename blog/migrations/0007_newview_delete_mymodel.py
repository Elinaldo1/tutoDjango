# Generated by Django 4.2.3 on 2023-09-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('frente', models.CharField(max_length=255)),
                ('localizacao', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]