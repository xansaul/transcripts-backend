from rest_framework.viewsets import ModelViewSet
from .models import VideoTranscription
from .serializers import VideoInfoSerialize


class VideosTxtsApi(ModelViewSet):
    queryset = VideoTranscription.objects.all()
    serializer_class = VideoInfoSerialize
    
            