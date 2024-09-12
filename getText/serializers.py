from rest_framework import serializers
from .models import VideoTranscription


class UrlSerializer(serializers.Serializer):
    url = serializers.URLField()
    
    
class VideoInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VideoTranscription
        fields = '__all__'