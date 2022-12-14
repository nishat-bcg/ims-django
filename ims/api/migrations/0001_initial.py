# Generated by Django 4.1 on 2022-08-25 06:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "first_name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]*$", "Only characters are allowed."
                            )
                        ],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]*$", "Only characters are allowed."
                            )
                        ],
                    ),
                ),
                ("address", models.TextField(blank=True, max_length=300, null=True)),
                (
                    "phone",
                    models.CharField(
                        max_length=12,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
            options={
                "verbose_name_plural": "Customers",
            },
        ),
        migrations.CreateModel(
            name="CustomerGroup",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "CustomerGroups",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "price",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="api.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=250)),
                ("phone", models.CharField(max_length=14)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "verbose_name_plural": "Suppliers",
            },
        ),
        migrations.CreateModel(
            name="ProductOrder",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("order_discount", models.PositiveIntegerField()),
                ("total_price", models.PositiveIntegerField()),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to="api.customer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="api.product",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "ProductOrders",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="supplier",
                to="api.supplier",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group",
                to="api.customergroup",
            ),
        ),
    ]
