import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Fungsi untuk mendapatkan semua data komentar dari video YouTube
def get_all_comments(video_id, api_key):
    try:
        # Membangun objek YouTube Data API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Mengirim permintaan API untuk mendapatkan komentar video
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100
        ).execute()

        # Mendapatkan semua komentar dari respons API
        comments = []
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append(comment)

        return comments

    except HttpError as e:
        print(f'Error: {e}')
        return None

# Setel video ID dan kunci API Anda
video_id = 'YRaJa-VjLGE'
api_key = 'API_KEY' # Masukan api key anda disini

# Panggil fungsi untuk mendapatkan semua data komentar
comment_data = get_all_comments(video_id, api_key)

# Menyimpan data komentar ke dalam file CSV dengan nama file sesuai dengan ID view
filename = f'{video_id}_comment_data.csv'
fieldnames = ['Comment', 'Likes']

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for comment in comment_data:
        comment_text = comment['textDisplay']
        like_count = comment['likeCount']

        writer.writerow({'Comment': comment_text, 'Likes': like_count})

print(f"Data komentar telah disimpan ke dalam file '{filename}'.")
