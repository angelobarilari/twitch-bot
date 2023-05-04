from django.db import models
import uuid

class Message(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    author = models.CharField(max_length=255)
    channel = models.CharField(max_length=255)
    original_message = models.TextField()
    generated_verse = models.TextField()
    timestamp = models.DateTimeField()