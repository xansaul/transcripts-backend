from django.db import models
import uuid

class VideoTranscription(models.Model):
    title = models.CharField(max_length=250)
    upload_date = models.DateField()

    def __str__(self):
        return f"{self.title}"
    
    
class TxtFile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    video = models.ForeignKey(VideoTranscription,on_delete=models.CASCADE)