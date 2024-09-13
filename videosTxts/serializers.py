from rest_framework import serializers
from .models import VideoTranscription, TxtFile

class TxtFileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = TxtFile
        fields = ['id', 'video', 'url']
        
    def get_url(self, obj):
        return f"/media/texts/{obj.id}.txt"

class VideoInfoSerialize(serializers.ModelSerializer):
    upload_date = serializers.DateField(
        input_formats=['%d/%m/%y', '%d/%m/%Y'],
        format='%d/%m/%Y'
    )
    txt_file = TxtFileSerializer(source='txtfile_set', many=True) 

    class Meta:
        model = VideoTranscription
        fields = ['title', 'upload_date', 'txt_file'] 
