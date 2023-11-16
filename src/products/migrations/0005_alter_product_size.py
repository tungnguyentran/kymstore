# Generated by Django 4.2.7 on 2023-11-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_product_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="size",
            field=models.CharField(
                choices=[
                    ("XS", "XS"),
                    ("S", "S"),
                    ("M", "M"),
                    ("L", "L"),
                    ("XL", "XL"),
                ],
                default="XS",
                max_length=20,
            ),
        ),
    ]
