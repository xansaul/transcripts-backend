import yt_dlp
import uuid

def download_youtube_audio(url, output_path):
    audio_title = uuid.uuid4()
    video_info = {
        "title": "",
        "upload_date": "",
        "audio_id": audio_title
    }
    ydl_opts = {
        'format': 'bestaudio/best',  # Descargar el mejor audio disponible
        'outtmpl': f'{output_path}/{audio_title}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',  # Puedes cambiarlo a 'wav', 'm4a', etc.
            'preferredquality': '192',  # Calidad del audio (192 kbps en este caso)
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        
        video_title = info_dict.get('title', 'Desconocido')
        upload_date = info_dict.get('upload_date', 'Desconocida')
        
        formatted_date = (
            f"{upload_date[6:]}/{upload_date[4:6]}/{upload_date[2:4]}"
            if upload_date != 'Desconocida' else upload_date
        )
        
        video_info['title'] = video_title
        video_info['upload_date'] = formatted_date
        

    return video_info


if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=-9g5gStDVkE'
    output_path = './'
    
    download_youtube_audio(video_url, output_path)
