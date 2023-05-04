# Generated by Django 4.2 on 2023-05-04 20:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('channel', models.CharField(max_length=255)),
                ('original_message', models.TextField()),
                ('generated_verse', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]