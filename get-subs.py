from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Fungsi untuk mendapatkan jumlah subscriber dan jumlah video dari saluran YouTube
def get_channel_stats(channel_id, api_key):
    try:
        # Membangun objek YouTube Data API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Mengirim permintaan API untuk mendapatkan informasi saluran
        response = youtube.channels().list(
            part='statistics',
            id=channel_id
        ).execute()

        # Mendapatkan jumlah subscriber dan jumlah video dari respons API
        subscriber_count = response['items'][0]['statistics']['subscriberCount']
        video_count = response['items'][0]['statistics']['videoCount']
        return subscriber_count, video_count

    except HttpError as e:
        print(f'Error: {e}')
        return None, None

# Setel channel ID dan kunci API Anda
channel_id = 'UC_9oL2jwz-w2VeaXz9eDakQ'
api_key = 'API_KEY' # Masukan api key anda disini

# Panggil fungsi untuk mendapatkan jumlah subscriber dan jumlah video
subscriber_count, video_count = get_channel_stats(channel_id, api_key)

# Cetak jumlah subscriber dan jumlah video
if subscriber_count is not None and video_count is not None:
    print(f'Jumlah Subscriber: {subscriber_count}')
    print(f'Jumlah Video: {video_count}')
