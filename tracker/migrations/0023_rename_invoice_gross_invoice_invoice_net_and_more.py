# Generated by Django 4.2 on 2024-08-08 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0022_alter_item_unit"),
    ]

    operations = [
        migrations.RenameField(
            model_name="invoice",
            old_name="invoice_gross",
            new_name="invoice_net",
        ),
        migrations.AddField(
            model_name="invoice",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="amount_received",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="provided_quantities",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]