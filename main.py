from src.cat_gif import saveCatGif
from src.top_music import saveTopSongText
from src.weather import saveWeatherText
from src.slack_send import slackNotification


def main():
    saveCatGif()
    saveTopSongText()
    saveWeatherText()
    slackNotification()


if __name__ == '__main__':
    main()
