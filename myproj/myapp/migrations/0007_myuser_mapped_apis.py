# Generated by Django 4.2.3 on 2023-07-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_myuser_options_alter_myuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='mapped_apis',
            field=models.ManyToManyField(blank=True, to='myapp.api'),
        ),
    ]
