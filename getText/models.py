from django.db import models
import uuid

# Create your models here.
class VideoTranscription(models.Model):
    title = models.CharField(max_length=250)
    upload_date = models.DateField()
    audio_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return f"{self.title}"