# Generated by Django 4.2 on 2024-08-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0025_invoice_invoice_gross"),
    ]

    operations = [
        migrations.AddField(
            model_name="contract",
            name="vat_percentage",
            field=models.DecimalField(decimal_places=2, default=19.0, max_digits=5),
        ),
    ]
