import requests
import smtplib
from email.mime.text import MIMEText
import os

API_KEY = os.environ['YOUTUBE_API_KEY']
CHANNEL_ID = os.environ['CHANNEL_ID']
EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

def get_latest_video():
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&order=date&part=snippet'
    response = requests.get(url).json()
    return response['items'][0]['id']['videoId']

def send_email(video_id):
    msg = MIMEText(f'New video uploaded: https://www.youtube.com/watch?v={video_id}')
    msg['Subject'] = 'New YouTube Video Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == '__main__':
    latest_video_id = get_latest_video()
    # 使用文件存储最新视频 ID
    try:
        with open('latest_video.txt', 'r') as f:
            last_video_id = f.read().strip()
    except FileNotFoundError:
        last_video_id = ''

    if latest_video_id != last_video_id:
        send_email(latest_video_id)
        with open('latest_video.txt', 'w') as f:
            f.write(latest_video_id)
