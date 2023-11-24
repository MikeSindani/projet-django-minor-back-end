# Generated by Django 4.1.7 on 2023-10-07 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minor_asset', '0006_remove_agent_user_remove_inventoryinto_user_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='agent',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='minor_asset.agent', unique=True),
            preserve_default=False,
        ),
    ]
