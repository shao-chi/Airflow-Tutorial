import requests
import json

from config import YOUTUBE_API_KEY
from utils.utils import textToTxt


def saveTopSongText():
    textToTxt(getTopSongInfo, 'song.txt')


def getTopSongInfo():
    url = f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&chart=mostPopular&regionCode=TW&videoCategoryId=10&key={YOUTUBE_API_KEY}"

    response = requests.get(url)
    topSong = json.loads(response.text)['items'][0]
    video_id = topSong['id']
    title = topSong['snippet']['title']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    return f"今天 Youtube Trend Music Top 1: {title} ({video_url})"
