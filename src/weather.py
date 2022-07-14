import requests
import json
# from datetime import datetime

from config import WEATHER_API_AUTHORIZATION
from utils.utils import textToTxt


def saveWeatherText():
    textToTxt(getWeatherText, 'weather.txt')


def getWeatherText():

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": WEATHER_API_AUTHORIZATION,
        "locationName": "臺北市",
        # "endTime": datetime.now().strftime("%Y-%m-%d") + "T06:00:00"
    }

    response = requests.get(url, params=params)
    # print(response.status_code)

    if response.status_code == 200:
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]
        elements = data["records"]["location"][0]["weatherElement"]
        elements = [e["time"][0]["parameter"]["parameterName"]
                    for e in elements]

        state = f'今天{location}的天氣 {elements[0]}, 你會感到 {elements[3]}'
        prob = f'總之呢, 降雨機率 {elements[1]} %'
        temp = f'最低溫度 {elements[2]} 度, 最高溫度 {elements[4]} 度'
        return f'{state}\n{prob}, {temp}'

    return None
