# Generated by Django 4.2.3 on 2023-07-29 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_api_created_by_alter_myuser_mapped_apis'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
