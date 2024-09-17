from ..use_cases import audio_to_text, get_audio_from_youtube
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

OUTPUT_PATH_AUDIO = './audio'

def process_video(url):
    audio_info = get_audio_from_youtube.download_youtube_audio(url, OUTPUT_PATH_AUDIO)
    video_uuid = audio_info.get("video_uuid")
    audio_path = f"./audio/{video_uuid}.flac"
    
    text = audio_to_text.transcribe_audio(audio_path)
    delete_generated_audio(audio_path)
    
    return {
        'text': text,
        **audio_info
    }


def chunk_videos(videos, chunk_size=2):
    for i in range(0, len(videos), chunk_size):
        yield videos[i:i + chunk_size]


def delete_generated_audio(audio_path):
    os.remove(audio_path)
    
def process_videos_in_parallel(videos_urls):
    videos_info = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        for video_pair in chunk_videos(videos_urls):
            futures = [executor.submit(process_video, url) for url in video_pair]
            for future in as_completed(futures):
                videos_info.append(future.result())
    return videos_info