# Generated by Django 4.2.1 on 2023-05-09 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("datacollector", "0011_alter_message_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 9, 19, 29, 12, 340000, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
