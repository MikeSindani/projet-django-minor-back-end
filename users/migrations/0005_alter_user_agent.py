# Generated by Django 4.1.7 on 2023-10-08 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_team_agent_user_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.agent'),
        ),
    ]