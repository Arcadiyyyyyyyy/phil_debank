from telegram_bot.bot.src.exceptions.back_end.DebankAPI import DebankAPIError
import requests


def get_feed_hot_list():
    response = requests.get("https://api.debank.com/feed/hot_list?limit=100")

    if response.status_code == 200:
        return response.json()
    else:
        raise DebankAPIError("Status code is not 200")
