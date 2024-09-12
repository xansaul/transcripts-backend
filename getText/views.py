from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UrlSerializer
from .use_cases import audio_to_text, get_audio_from_youtube
from .use_cases.get_urls_from_playlist import get_playlist_videos

OUTPUT_PATH_AUDIO = './audio'

class GetTextApi(APIView):

    def post(self, request):
        
        data = UrlSerializer(data=request.data)
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        
        videos_urls = get_playlist_videos(data.validated_data.get("url"))
        videos_info = []
        
        for url in videos_urls:
            audio_info = get_audio_from_youtube.download_youtube_audio(url, OUTPUT_PATH_AUDIO)
            audio_id = audio_info.get("audio_id")
            text = audio_to_text.transcribe_audio(f"./audio/{audio_id}.wav")
            videos_info.append({
                'text': text,
                **audio_info
            })
        
        return Response({
            "videos": videos_info
        })
