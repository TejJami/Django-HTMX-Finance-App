# Generated by Django 4.2 on 2024-08-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0023_rename_invoice_gross_invoice_invoice_net_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="amount_received",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
