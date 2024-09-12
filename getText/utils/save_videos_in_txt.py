import os
from django.conf import settings

def save_txt(content, file_name):
    try:
        
        file_path = os.path.join(settings.MEDIA_ROOT, 'texts', f"{file_name}.txt")
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print(f"Content saved successfully to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def save_videos(videos):
    
    for video_info in videos:
        audio_id =  f"{video_info.get('audio_id')}"
        text = f"""
{video_info.get('title')}
{video_info.get('upload_date')}
{video_info.get('text')}
"""
        save_txt(text, audio_id)  
