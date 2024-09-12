import json
from django.http import StreamingHttpResponse
from concurrent.futures import ThreadPoolExecutor, as_completed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import VideoInfoSerializer

from .serializers import UrlSerializer
from .use_cases.get_urls_from_playlist import get_playlist_videos

from .utils.video_processing import process_video, chunk_videos
from .utils.save_videos_in_txt import save_videos
class GetTextApi(APIView):

    def post(self, request):
        data = UrlSerializer(data=request.data)
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        
        videos_urls = get_playlist_videos(data.validated_data.get("url"))
        videos_info = []
       
        with ThreadPoolExecutor() as executor:
            for video_pair in chunk_videos(videos_urls, 3):
                futures = [executor.submit(process_video, url) for url in video_pair]
                for future in as_completed(futures):
                    videos_info.append(future.result())
        
        
        save_videos(videos_info)

        videos_data = VideoInfoSerializer(data=videos_info, many=True)
        if not videos_data.is_valid():
            print(videos_data.errors)
            return Response({
                "errors": videos_data.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
        videos_data.save()
        
        return Response({
            "videos": videos_data.data
        })


class GetTextApiStream(APIView):

    def post(self, request):
        data = UrlSerializer(data=request.data)
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        
        videos_urls = get_playlist_videos(data.validated_data.get("url"))

        def stream_videos():
            with ThreadPoolExecutor() as executor:
                for video_pair in chunk_videos(videos_urls, 3):
                    futures = [executor.submit(process_video, url) for url in video_pair]
                    for future in as_completed(futures):
                        video_info = future.result()
                        yield json.dumps({
                            "video": video_info
                        }) + "\n"

        return StreamingHttpResponse(stream_videos(), content_type="application/json")
