# Generated by Django 4.2.3 on 2023-07-28 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_user_myuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='User',
        ),
    ]
