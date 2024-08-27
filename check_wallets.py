import requests
import datetime
from open_txt import api_key
from pprint import pprint

class Coin:
    def __init__(self, coin):
        self.address_coin = coin['coin_type']
        self.amount_coin = float(coin['amount']) / 100000000
        name_coin = coin['coin_type'].split('::')
        self.name_coin = name_coin[2]
        token_price = requests.get(
            f'https://api.geckoterminal.com/api/v2/simple/networks/aptos/token_price/{self.address_coin}').json()
        try:
            self.price = float(token_price['data']['attributes']['token_prices'][f'{self.address_coin}'])
            self.usd_value = self.price * self.amount_coin
        except KeyError as e:
            self.usd_value = 0.0
            # self.price = f'Нет цены для {self.amount_coin} {self.name_coin}'


class WalletCoins:
    # получаем список и количество монет в кошельке

    def __init__(self, wallet='0x58bdeb346ae023ecb659c4a09a840e0703c9b2665c2288f2e225d07ad1a9f724', limit=25):
        self.wallet = wallet
        self.limit = limit
        self._api_key = api_key
        self.headers = {"accept": "application/json", "X-API-Key": self._api_key}
        self.params = {"limit": limit, "owner_addresses[0]": self.wallet}
        url_coins = "https://mainnet-aptos-api.moralis.io/wallets/coins"
        dict_response = requests.get(url=url_coins, headers=self.headers, params=self.params).json()

        print(f'в кошельке {self.wallet} на {datetime.date.today()}:')
        self.dict_response = dict_response['result']
        # pprint(self.dict_response)

    def check_tokens(self):
        dict_tokens = {}
        for coin in self.dict_response:
            coin_class = Coin(coin)
            if coin_class.usd_value > 0:
                print(f'{coin_class.amount_coin} {coin_class.name_coin} = {coin_class.usd_value:3f} usd')
            else:
                print(f'Нет цены для {coin_class.amount_coin} {coin_class.name_coin}')

            dict_tokens[coin_class.name_coin] = coin_class.usd_value

            total_tokens = float(sum(dict_tokens.values()))
            # return f'Итого в кошельке: {sum_usd:3f} USD'

        print(f'Итого в кошельке монет на сумму {total_tokens:3f} USD:')

    def check_nft(self):
        dict_nfts = {}
        url_nft = "https://mainnet-aptos-api.moralis.io/wallets/nfts"
        dict_response = requests.get(url=url_nft, headers=self.headers, params=self.params).json()
        print(f'в кошельке {self.wallet}:')
        print()

        for token in dict_response['result']:
            name_nft = token["collection_name"]

            if "collection_name" in token:
                # print(f'{token["collection_name"]}')
                if name_nft not in dict_nfts:
                    dict_nfts[name_nft] = 1
                else:
                    dict_nfts[name_nft] += 1
        total_nfts = sum(dict_nfts.values())

        print(f'всего в кошельке {total_nfts} NFT:')
        print(*dict_nfts.items(), sep='\n')
