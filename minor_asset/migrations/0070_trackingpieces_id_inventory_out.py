# Generated by Django 4.2.7 on 2024-04-06 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minor_asset', '0069_remove_trackingpieces_id_inventory_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackingpieces',
            name='id_inventory_out',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='minor_asset.inventoryout'),
        ),
    ]
