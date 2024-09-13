from rest_framework import serializers
from .models import TxtFile, VideoTranscription

class TxtFileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = TxtFile
        fields = ['id', 'url']
        
    def get_url(self, obj):
        return f"/media/texts/{obj.id}.txt"

class VideoInfoSerializer(serializers.ModelSerializer):
    upload_date = serializers.DateField(
        input_formats=['%d/%m/%y', '%d/%m/%Y'],
        format='%d/%m/%Y'
    )
    txt_file = TxtFileSerializer()  

    class Meta:
        model = VideoTranscription
        fields = ['id','title', 'upload_date', 'txt_file', 'text']
