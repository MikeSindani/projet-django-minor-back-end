# Generated by Django 4.1.7 on 2023-10-08 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_agent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='agent',
        ),
    ]