# Generated by Django 4.2.6 on 2023-10-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor_asset', '0037_rename_asset_code_client_id_machine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='price_after_conversion',
        ),
        migrations.RemoveField(
            model_name='inventoryinto',
            name='price_after_conversion',
        ),
        migrations.AddField(
            model_name='inventory',
            name='price_used_by_entreprise',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='inventoryinto',
            name='price_used_by_entreprise',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='capacity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryinto',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryinto',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]
