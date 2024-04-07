# Generated by Django 5.0.4 on 2024-04-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="discount",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="item",
            name="retailer",
            field=models.CharField(default="ecommerce", max_length=100),
        ),
        migrations.AddField(
            model_name="item",
            name="return_policy",
            field=models.CharField(
                choices=[
                    ("return_refund", "Eligible for return and refund"),
                    ("return_partial_refund", "Eligible for return and partial refund"),
                    ("no_return_refund", "Not eligible for return and refund"),
                ],
                default="return_refund",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="stock",
            field=models.IntegerField(default=0),
        ),
    ]