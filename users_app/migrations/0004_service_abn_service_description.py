# Generated by Django 5.1.1 on 2024-09-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_service_service_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='ABN',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
