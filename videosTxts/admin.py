from django.contrib import admin
from .models import VideoTranscription, TxtFile

# Register your models here.
admin.site.register(VideoTranscription)
admin.site.register(TxtFile)