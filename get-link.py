from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Fungsi untuk mendapatkan daftar link video dari hasil pencarian YouTube
def search_youtube_videos(query, api_key):
    try:
        # Membangun objek YouTube Data API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Mengirim permintaan API untuk melakukan pencarian video
        response = youtube.search().list(
            part='id',
            q=query,
            type='video',
            maxResults=10
        ).execute()

        # Mendapatkan daftar link video dari respons API
        video_links = []
        for item in response['items']:
            video_id = item['id']['videoId']
            video_links.append(f'https://www.youtube.com/watch?v={video_id}')

        return video_links

    except HttpError as e:
        print(f'Error: {e}')
        return None

# Setel query pencarian dan kunci API Anda
query = 'programming tutorials'
api_key = 'API_KEY' # Masukan api key anda disini

# Panggil fungsi untuk melakukan pencarian dan mendapatkan daftar link video
video_links = search_youtube_videos(query, api_key)

# Cetak daftar link video
for link in video_links:
    print(link)
