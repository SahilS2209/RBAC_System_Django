# Generated by Django 4.2.3 on 2023-07-31 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_api_mapped_users_alter_myuser_mapped_apis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='mapped_users',
        ),
    ]