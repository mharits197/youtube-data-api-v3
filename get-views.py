from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Fungsi untuk mendapatkan statistik video dari YouTube
def get_video_stats(video_id, api_key):
    try:
        # Membangun objek YouTube Data API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Mengirim permintaan API untuk mendapatkan statistik video
        response = youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        # Mendapatkan jumlah like, dislike, komentar, dan tampilan (views) dari respons API
        like_count = response['items'][0]['statistics']['likeCount']
        # dislike_count = response['items'][0]['statistics']['dislikeCount']
        comment_count = response['items'][0]['statistics']['commentCount']
        view_count = response['items'][0]['statistics']['viewCount']
        return like_count, comment_count, view_count

    except HttpError as e:
        print(f'Error: {e}')
        return None, None, None, None
# JK54hrdz5Zk
# Setel video ID dan kunci API Anda
video_id = 'd8RYu67CLEY'
api_key = 'API_KEY' # Masukan api key anda disini

# Panggil fungsi untuk mendapatkan statistik video
like_count, comment_count, view_count = get_video_stats(video_id, api_key)

# Cetak statistik video
if like_count is not None and comment_count is not None and view_count is not None:
    print(f'Jumlah Like: {like_count}')
    # print(f'Jumlah Dislike: {dislike_count}')
    print(f'Jumlah Komentar: {comment_count}')
    print(f'Jumlah Tampilan: {view_count}')
