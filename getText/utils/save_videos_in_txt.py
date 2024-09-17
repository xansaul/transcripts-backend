import os
from django.conf import settings
from videosTxts.models import TxtFile, VideoTranscription
from datetime import datetime
import re

TXTS_PATH = os.path.join(settings.MEDIA_ROOT, 'texts')


def remove_repetitions(text):
    text = re.sub(r'\b(\w+)([\s.,;!?\']+\1)+\b', r'\1', text)
    
    text = re.sub(r'\b((?:\w+[\s.,;!?\']+){0,3}\w+)([\s.,;!?\']+\1)+\b', r'\1', text)
    
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\s([.,;!?\'])', r'\1', text)
    
    text = re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', text)
    text = re.sub(r'\b((?:\w+\s+){0,10}\w+)(?:\s+\1)+\b', r'\1', text)
    
    return text



def create_txt(content, file_name):
    try:
        file_path = os.path.join(TXTS_PATH, f"{file_name}.txt")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print(f"Content saved successfully to {file_path}")
    except IOError as e:
        print(f"File error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def save_videos_and_generate_text_files(videos):
    txts_objects = []
    video_objects = []
    
    for video in videos:
        try:
            upload_date = datetime.strptime(video.get('upload_date'), "%d/%m/%Y").date()
            title = video.get('title')
            text=video.get('text').strip()
            url = video.get('url')
            video_db = VideoTranscription(title=title, upload_date=upload_date, text=text, url=url)
            video_objects.append(video_db)
            
            
            txt = TxtFile()  
            txts_objects.append(txt)
            
        except ValueError as e:
            print(f"Date parsing error: {e}")
            continue

    
    for video_db, txt in zip(video_objects, txts_objects):
        video_db.txt_file = txt
        
        template = f"""{video_db.title}
{video_db.upload_date.strftime('%d/%m/%Y')}
{remove_repetitions(video_db.text)}
        """
        create_txt(template, txt.id)

        txt.save()

    VideoTranscription.objects.bulk_create(video_objects)
    
    return video_objects


def delete_txt(id):
    os.remove(os.path.join(TXTS_PATH, f"{id}.txt"))
