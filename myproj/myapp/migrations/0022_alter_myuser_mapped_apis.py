# Generated by Django 4.2.3 on 2023-07-31 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_remove_api_mapped_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mapped_apis',
            field=models.ManyToManyField(to='myapp.api'),
        ),
    ]
