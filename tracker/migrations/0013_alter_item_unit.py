# Generated by Django 4.2 on 2024-08-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0012_rename_budget_item_quantity_item_rate_item_total_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="unit",
            field=models.CharField(
                choices=[("Std.", "Std."), ("Psch", "Psch")],
                default="Std.",
                max_length=10,
            ),
        ),
    ]