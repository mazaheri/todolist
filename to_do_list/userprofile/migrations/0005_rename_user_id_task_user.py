# Generated by Django 4.2.4 on 2023-09-05 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_rename_user_task_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user_id',
            new_name='user',
        ),
    ]