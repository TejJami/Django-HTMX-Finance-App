# Generated by Django 4.2 on 2025-01-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0031_item_order_section_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="EstimateInvoiceSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "consecutive_start_no",
                    models.IntegerField(
                        default=1,
                        help_text="Starting number for consecutive numbering.",
                    ),
                ),
                (
                    "terms_and_conditions_files",
                    models.FileField(
                        blank=True,
                        help_text="Upload Word files for terms and conditions.",
                        null=True,
                        upload_to="terms_and_conditions/",
                    ),
                ),
                (
                    "selected_terms",
                    models.CharField(
                        blank=True,
                        help_text="Selected terms and conditions file.",
                        max_length=255,
                    ),
                ),
                (
                    "bck_eng_template",
                    models.FileField(
                        blank=True, null=True, upload_to="templates/estimates/"
                    ),
                ),
                (
                    "bck_de_template",
                    models.FileField(
                        blank=True, null=True, upload_to="templates/estimates/"
                    ),
                ),
                (
                    "kost_eng_template",
                    models.FileField(
                        blank=True, null=True, upload_to="templates/estimates/"
                    ),
                ),
                (
                    "kost_de_template",
                    models.FileField(
                        blank=True, null=True, upload_to="templates/estimates/"
                    ),
                ),
                (
                    "inv_bck_eng_template",
                    models.FileField(
                        blank=True, null=True, upload_to="templates/invoices/"
                    ),
                ),
                (
                    "inv_bck_de_template",
                    models.FileField(
                        blank=True, null=True, upload_to="templates/invoices/"
                    ),
                ),
                (
                    "inv_kost_eng_template",
                    models.FileField(
                        blank=True, null=True, upload_to="templates/invoices/"
                    ),
                ),
                (
                    "inv_kost_de_template",
                    models.FileField(
                        blank=True, null=True, upload_to="templates/invoices/"
                    ),
                ),
            ],
        ),
    ]