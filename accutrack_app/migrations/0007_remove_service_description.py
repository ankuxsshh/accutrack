# Generated by Django 5.1 on 2025-01-18 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accutrack_app', '0006_alter_service_options_remove_service_image_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
    ]
