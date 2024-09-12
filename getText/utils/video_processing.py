from ..use_cases import audio_to_text, get_audio_from_youtube
import os

OUTPUT_PATH_AUDIO = './audio'

def process_video(url):
    audio_info = get_audio_from_youtube.download_youtube_audio(url, OUTPUT_PATH_AUDIO)
    audio_id = audio_info.get("audio_id")
    audio_path = f"./audio/{audio_id}.wav"
    
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
    