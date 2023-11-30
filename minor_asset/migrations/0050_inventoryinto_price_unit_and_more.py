# Generated by Django 4.2.7 on 2023-11-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor_asset', '0049_delete_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryinto',
            name='price_unit',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='inventoryinto',
            name='price_unit_used_by_entreprise',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]
