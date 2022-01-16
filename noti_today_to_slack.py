import requests
import json
import os
from datetime import datetime

"""
매분마다 특정 스크립트를 실행하고 로그를 남긴다.
* * * * * /usr/local/bin/python ~/Desktop/noti_today_to_slack.py >> ~/Desktop/noti_today_to_slack.log 2>&1
"""

URL = os.getenv("URL")


def send_to_slack(message):
    print(message)
    response = requests.post(
        URL, headers={"Content-type": "application/json"}, data=json.dumps(message))
    print(response.status_code)
    print(response.text)


def today_bot():
    print
    today = datetime.today()
    print(today)
    send_to_slack(
        {"text": f"{today.year}/{today.month}/{today.day} {today.hour}:{today.minute}:{today.second}"})


if __name__ == "__main__":
    print("Hi")
    today_bot()
    print("Bye")
