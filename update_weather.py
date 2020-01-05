from typing import Dict
import json
from os import environ as env
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests


def get_weather() -> Dict:
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(
        env['DARKSKY_TOKEN'], env['LATITUDE'], env['LONGITUDE']
    )
    params = {
        'exclude': ['minutely', 'hourly', 'daily', 'alerts', 'flags'],
        'lang': 'en',
        'units': env['UNITS']
    }
    return requests.get(url=url, params=params).json()['currently']


def get_unit_letter() -> str:
    if env['UNITS'] in ('si', 'ca', 'uk2'):
        return 'C'
    elif env['UNITS'] == 'us':
        return 'F'
    else:
        raise SystemError('Unknown unit system: `{}`'.format(env['UNITS']))


def set_slack_status(text: str, emoji: str) -> None:
    url = 'https://slack.com/api/users.profile.set'
    profile = {
        'status_text': text,
        'status_emoji': emoji,
        'status_expiration': 0
    }
    fields = {
        'profile': profile,
        'token': env['SLACK_TOKEN']
    }
    req = Request(url, urlencode(fields).encode())
    assert json.loads(urlopen(req).read().decode())['ok']


def icon_to_emoji(icon: str) -> str:
    MAPPING = {
        'clear-day': ':sunny:',
        'clear-night': ':last_quarter_moon_with_face:',
        'rain': ':rain_cloud:',
        'snow': ':snowflake:',
        'sleet': ':snow_cloud:',
        'wind': ':dash:',
        'fog': ':fog:',
        'cloudy': ':cloud:',
        'partly-cloudy-day': ':partly_sunny:',
        'partly-cloudy-night': ':last_quarter_moon_with_face:',
        'default': ':red_circle:'
    }
    return MAPPING[icon] if icon in MAPPING else MAPPING['default']


def update_weather() -> None:
    weather = get_weather()
    temperature = round(weather['temperature'])
    emoji = icon_to_emoji(weather['icon'])
    status = {
        'text': '{}°{}'.format(temperature, get_unit_letter()),
        'emoji': emoji
    }
    set_slack_status(**status)
    print(status)


if __name__ == "__main__":
    update_weather()
