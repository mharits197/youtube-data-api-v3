import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from urllib.parse import urlencode, quote

# Fungsi untuk mendapatkan data dari hasil pencarian YouTube
def get_search_results(keyword, api_key):
    try:
        # Membangun objek YouTube Data API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Mengirim permintaan API untuk melakukan pencarian
        response = youtube.search().list(
            q=keyword,
            part='snippet',
            type='video',
            maxResults=10
        ).execute()

        # Mendapatkan hasil pencarian video
        videos = []
        for item in response['items']:
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_author = item['snippet']['channelTitle']

            # Mengirim permintaan API untuk mendapatkan statistik video
            video_stats = youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()

            # Memeriksa apakah data statistik video tersedia
            if 'items' in video_stats and len(video_stats['items']) > 0:
                video_stats = video_stats['items'][0]['statistics']
                video_views = video_stats.get('viewCount', 'N/A')
                video_likes = video_stats.get('likeCount', 'N/A')
                video_comments = video_stats.get('commentCount', 'N/A')
            else:
                video_views = 'N/A'
                video_likes = 'N/A'
                video_comments = 'N/A'

            video_data = {
                'Video ID': f'https://www.youtube.com/watch?v={video_id}',
                'Title': video_title,
                'Author': video_author,
                'Views': video_views,
                'Likes': video_likes,
                'Comments': video_comments
            }
            videos.append(video_data)

        return videos

    except HttpError as e:
        print(f'Error: {e}')
        return None

# Setel keyword pencarian dan kunci API Anda
keyword = 'Debian Indonesia'
api_key = 'API_KEY' # Masukan api key anda disini

# Panggil fungsi untuk mendapatkan data dari hasil pencarian
search_results = get_search_results(keyword, api_key)

# Menyimpan data hasil pencarian ke dalam file CSV
filename = f'{quote(keyword)}_search_results.csv'
fieldnames = ['Video ID', 'Title', 'Author', 'Views', 'Likes', 'Comments']

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for video in search_results:
        writer.writerow(video)

print(f"Data hasil pencarian telah disimpan ke dalam file '{filename}'.")
