#!usr/bin python 3.8
import requests
import random
import string
import json

PLATFORM_API_URL = "https://br1.api.riotgames.com"
REGIONAL_API_URL = "https://americas.api.riotgames.com"
API_KEY = "RGAPI-9c88f5f3-dbd8-409c-892c-97eab34d5119"


def create_tournament_code(qtd=1):
    url = REGIONAL_API_URL + "/lol/tournament-stub/v4/codes"

    params = {
        'count': qtd,
        'tournamentId': ''.join(random.choices(string.digits, k=25)),
        "api_key": API_KEY
    }

    body = {
      "mapType": "SUMMONERS_RIFT",
      "pickType": "TOURNAMENT_DRAFT",
      "spectatorType": "ALL",
      "teamSize": 5
    }

    payload = requests.post(url, params=json.dumps(params), data=body)

    print('Url: ' + payload.url + ' response ' + payload.text)


def create_tournament_providers():
    url = REGIONAL_API_URL + "/lol/tournament-stub/v4/providers"

    params = {
        "api_key": API_KEY
    }

    body = {
        "region": "BR",
        "url": "https://teste.com"
    }

    response = requests.post(url, params=params, data=json.dumps(body))


def main():
    create_tournament_providers()


if __name__ == "__main__":
    main()
