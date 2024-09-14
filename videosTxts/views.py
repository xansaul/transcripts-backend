from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import VideoTranscription
from .serializers import VideoInfoSerializer

from getText.utils.save_videos_in_txt import delete_txt

class VideosTxtsApi(ModelViewSet):
    queryset = VideoTranscription.objects.all()
    serializer_class = VideoInfoSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        delete_txt(instance.txt_file.id)
        
        self.perform_destroy(instance)
        
        return Response(status=status.HTTP_204_NO_CONTENT)