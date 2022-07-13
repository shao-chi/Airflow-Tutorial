from slack import WebClient

from config import SLACK_CHANNEL_ID
from config import SLACK_TOKEN


def slackNotification():
    client = WebClient(token=SLACK_TOKEN)

    with open('weather.txt', 'r') as f:
        weatherText = f.read()

    with open('song.txt', 'r') as f:
        songText = f.read()

    message = f"{weatherText}\n{songText}"
    client.files_upload(
        channels=SLACK_CHANNEL_ID,
        file="cat.gif",
        title="cat"
    )
    client.chat_postMessage(
        channel=SLACK_CHANNEL_ID,
        text=message
    )
