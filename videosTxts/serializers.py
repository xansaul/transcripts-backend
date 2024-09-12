from rest_framework import serializers
from .models import VideoTranscription


class VideoInfoSerializer(serializers.ModelSerializer):
    upload_date = serializers.DateField(
        input_formats=['%d/%m/%y', '%d/%m/%Y'],
        format='%d/%m/%Y'
    )
    txt_file = serializers.SerializerMethodField()
    
    def get_txt_file(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f"/media/txts/{obj.audio_id}.txt")
        return f"/media/txts/{obj.audio_id}.txt"
    
    class Meta:
        model = VideoTranscription
        fields = '__all__'
        
        