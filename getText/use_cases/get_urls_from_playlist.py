import yt_dlp

def get_playlist_videos(playlist_url):
    ydl_opts = {
        'skip_download': True,  
        'extract_flat': 'in_playlist',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
        
        video_urls = []
        if 'entries' in playlist_info:
            for video in playlist_info['entries']:
                video_url = video.get('url')
                if video_url:
                    video_urls.append(f"https://www.youtube.com/watch?v={video['id']}")
        else:
            video_urls.append(playlist_url)

    return video_urls

if __name__ == '__main__':
    playlist_url = 'https://www.youtube.com/watch?v=yv3_5jz-KAU&list=PLq1_FTkRbmQYa57jDWL9qtwRleLSmQIFc&pp=gAQBiAQB'
    
    video_urls = get_playlist_videos(playlist_url)
if __name__ == '__main__':
    urls = get_playlist_videos("https://www.youtube.com/watch?v=yv3_5jz-KAU&list=PLq1_FTkRbmQYa57jDWL9qtwRleLSmQIFc&pp=gAQBiAQB")
    print(urls)
