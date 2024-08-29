import requests


class CoinPrice:
    def __init__(self, address_coin):
        self.address_coin = address_coin['coin_type']
        self.amount_coin = float(address_coin['amount']) / 100000000
        name_coin = address_coin['coin_type'].split('::')
        self.name_coin = name_coin[2]
        token_price = requests.get(
            f'https://api.geckoterminal.com/api/v2/simple/networks/aptos/token_price/{self.address_coin}').json()
        try:
            self.price = float(token_price['data']['attributes']['token_prices'][f'{self.address_coin}'])
            self.usd_value = self.price * self.amount_coin
        except KeyError as e:
            self.usd_value = 0.0
