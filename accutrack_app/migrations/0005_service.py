# Generated by Django 5.1 on 2025-01-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accutrack_app', '0004_footercontent_email_footercontent_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('position', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]