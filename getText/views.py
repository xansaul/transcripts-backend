import json
from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

 
from .serializers import UrlSerializer
from .use_cases.get_urls_from_playlist import get_playlist_videos
from .utils.video_processing import process_videos_in_parallel
from .utils.save_videos_in_txt import save_videos_and_generate_text_files

from videosTxts.serializers import VideoInfoSerialize
from videosTxts.models import VideoTranscription



"""
    video_info = {
        "title": "",
        "upload_date": "",
        "video_uuid": video_uuid,
        "text": ""
    }

"""

class GetTextApi(APIView):

    def post(self, request):
        data = UrlSerializer(data=request.data)
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        
        videos_urls = get_playlist_videos(data.validated_data.get("url"))
        videos_info = process_videos_in_parallel(videos_urls)
        videos = save_videos_and_generate_text_files(videos_info)
        videos_serialized = VideoInfoSerialize(videos, many= True) 

        
        return Response({
            "videos":videos_serialized.data
        })


# class GetTextApiStream(APIView):

#     def post(self, request):
#         data = UrlSerializer(data=request.data)
#         if not data.is_valid():
#             return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         videos_urls = get_playlist_videos(data.validated_data.get("url"))

#         def stream_videos():
#             with ThreadPoolExecutor() as executor:
#                 for video_pair in chunk_videos(videos_urls, 3):
#                     futures = [executor.submit(process_video, url) for url in video_pair]
#                     for future in as_completed(futures):
#                         video_info = future.result()
#                         yield json.dumps({
#                             "video": video_info
#                         }) + "\n"

#         return StreamingHttpResponse(stream_videos(), content_type="application/json")



class Seed(APIView):
    
    def get(self, request):
        
        VideoTranscription.objects.all().delete()
        
        
        return Response(status=status.HTTP_200_OK)