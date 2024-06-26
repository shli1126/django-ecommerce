# Generated by Django 4.2.11 on 2024-04-10 22:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_item_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="start_date",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="order",
            name="ordered_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
