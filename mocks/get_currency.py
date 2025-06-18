import requests


def get_currency(coin_pair):
    resposta = requests.get(f"https://economia.awesomeapi.com.br/json/last/{coin_pair}")

    return resposta.json()
