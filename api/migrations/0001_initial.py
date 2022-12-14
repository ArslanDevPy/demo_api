# Generated by Django 4.1.3 on 2022-11-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShopModel",
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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
            ],
            options={
                "verbose_name": "Shop",
                "verbose_name_plural": "Shops",
                "db_table": "shop",
            },
        ),
        migrations.CreateModel(
            name="SupplierModel",
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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("address", models.TextField(verbose_name="Address")),
                (
                    "shop",
                    models.ManyToManyField(
                        related_name="supplier_shops", to="api.shopmodel"
                    ),
                ),
            ],
            options={
                "verbose_name": "Supplier",
                "verbose_name_plural": "Suppliers",
                "db_table": "supplier",
            },
        ),
    ]
