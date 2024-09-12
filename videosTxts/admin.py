from django.contrib import admin
from .models import VideoTranscription

# Register your models here.
class VideoModelAdmin(admin.ModelAdmin):
    readonly_fields = ('audio_id',)

admin.site.register(VideoTranscription, VideoModelAdmin)