# Generated by Django 4.2.1 on 2023-06-05 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("datacollector", "0003_alter_message_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023,
                    6,
                    5,
                    13,
                    29,
                    19,
                    350830,
                    tzinfo=datetime.timezone.utc,
                )
            ),
        ),
    ]
