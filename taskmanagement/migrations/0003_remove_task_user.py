# Generated by Django 5.0.4 on 2024-08-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0002_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
