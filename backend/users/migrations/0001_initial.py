# Generated by Django 4.2.2 on 2023-06-26 19:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("broadcaster_id", models.CharField(max_length=255)),
                ("broadcaster_login", models.CharField(max_length=255)),
                ("broadcaster_name", models.CharField(max_length=255)),
                ("broadcaster_language", models.CharField(max_length=255)),
                ("tags", models.JSONField(default=list)),
            ],
        ),
    ]
