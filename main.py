from src.catGif import saveCatGif
from src.topMusic import saveTopSongText
from src.weather import saveWeatherText
from src.slackSend import slackNotification


def main():
    saveCatGif()
    saveTopSongText()
    saveWeatherText()
    slackNotification()


if __name__ == '__main__':
    main()
