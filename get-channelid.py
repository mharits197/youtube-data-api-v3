from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from urllib.parse import urlparse

# Fungsi untuk mendapatkan channel ID dari URL saluran kustom
def get_channel_id(channel_url, api_key):
    try:
        # Mengurai URL saluran YouTube untuk mendapatkan nama pengguna
        url_components = urlparse(channel_url)
        username = url_components.path.strip('/@')

        # Membangun objek YouTube Data API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Mengirim permintaan API untuk mendapatkan informasi saluran berdasarkan nama pengguna
        response = youtube.channels().list(
            part='id',
            forUsername=username
        ).execute()

        # Mendapatkan channel ID dari respons API
        if 'items' in response and len(response['items']) > 0:
            channel_id = response['items'][0]['id']
            return channel_id
        else:
            print('Channel not found.')
            return None

    except HttpError as e:
        print(f'Error: {e}')
        return None

# Setel URL saluran kustom dan kunci API Anda
channel_url = 'https://youtube.com/channel/UC_9oL2jwz-w2VeaXz9eDakQ/'
api_key = 'API_KEY' # Masukan api key anda disini

# Panggil fungsi untuk mendapatkan channel ID
channel_id = get_channel_id(channel_url, api_key)

# Cetak channel ID
if channel_id is not None:
    print(f'Channel ID: {channel_id}')
