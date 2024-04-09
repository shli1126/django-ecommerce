# Generated by Django 4.2.11 on 2024-04-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_customuser_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
