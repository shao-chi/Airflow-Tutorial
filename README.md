# Airflow Demo

### Requirements
1. 取得各 API 授權
    * [Get Youtube Data API Key](https://hackmd.io/@c36ICNyhQE6-iTXKxoIocg/S1eYdtA1P#%E5%8F%96%E5%BE%97-Youtube-API_KEY)
    * [Get 中央氣象局 API Authorizatio](https://ithelp.ithome.com.tw/articles/10243411)
    * [Get Slack token & channel ID](https://blog.crazyfan.net/posts/2017/04/08/slack_incoming_webhooks/)
2. 建立 `config.py`
    ```python
    WEATHER_API_AUTHORIZATION = "{FILL HERE}"
    YOUTUBE_API_KEY = "{FILL HERE}"
    SLACK_TOKEN = "{FILL HERE}"
    SLACK_CHANNEL_ID = "{FILL HERE}"
    ```
