# Generated by Django 5.2.1 on 2025-05-09 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskModel',
            new_name='Task',
        ),
    ]
