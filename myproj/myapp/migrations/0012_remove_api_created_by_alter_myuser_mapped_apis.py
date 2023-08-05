# Generated by Django 4.2.3 on 2023-07-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_api_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='mapped_apis',
            field=models.ManyToManyField(blank=True, to='myapp.api'),
        ),
    ]