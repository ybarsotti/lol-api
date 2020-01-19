#!usr/bin python 3.8
import requests
import random
import string
import json

PLATFORM_API_URL = "https://br1.api.riotgames.com"
REGIONAL_API_URL = "https://americas.api.riotgames.com"
API_KEY = "SECRET"


def create_tournament(tournament_id):
    url = REGIONAL_API_URL + "/lol/tournament-stub/v4/codes"

    params = {
        'count': 2,
        'tournamentId': tournament_id,
        "api_key": API_KEY
    }

    body = {
      "mapType": "SUMMONERS_RIFT",
      "pickType": "TOURNAMENT_DRAFT",
      "spectatorType": "ALL",
      "teamSize": 5
    }

    response = requests.post(url, params=params, data=json.dumps(body))
    print(f"Sala de campeonato criada  / Código da sala: {response.text}")


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
    provider_id = response.text
    print('Provider ID: ' + provider_id)
    create_tournament_code(provider_id)


def create_tournament_code(provider_id):
    url = REGIONAL_API_URL + "/lol/tournament-stub/v4/tournaments"

    params = {
        "api_key": API_KEY
    }

    body = {
      "name": "PVT dos Suricatos",
      "providerId": provider_id
    }

    response = requests.post(url, params=params, data=json.dumps(body))
    print("Tournament Code: " + response.text)
    create_tournament(response.text)


def main():
    create_tournament_providers()


if __name__ == "__main__":
    main()
