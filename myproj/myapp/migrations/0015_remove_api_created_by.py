# Generated by Django 4.2.3 on 2023-07-29 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_api_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='created_by',
        ),
    ]