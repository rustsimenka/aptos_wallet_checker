import requests
import datetime
from pprint import pprint
from open_txt import api_key


class WalletCoins:
    # получаем список и количество монет в кошельке
    def __init__(self, wallet, limit=25):
        self.wallet = wallet
        self.limit = limit
        self._api_key = api_key
        self.headers = {"accept": "application/json", "X-API-Key": self._api_key}
        self.params = {"limit": limit, "owner_addresses[0]": self.wallet}

    def check_token(self):
        url_coins = "https://mainnet-aptos-api.moralis.io/wallets/coins"
        dict_response = requests.get(url=url_coins, headers=self.headers, params=self.params).json()

        print(f'в кошельке {self.wallet} на {datetime.date.today()}:')
        print()
        sum_usd = 0.0
        dict_tokens = {}

        for coin in dict_response['result']:
            address_coin = coin['coin_type']
            amount_coin = float(coin['amount']) / 100000000
            name_coin = coin['coin_type'].split('::')
            name_coin = name_coin[2]

            token_price = requests.get(f'https://api.geckoterminal.com/api/v2/simple/networks/aptos/token_price/{address_coin}').json()

            try:
                price = float(token_price['data']['attributes']['token_prices'][f'{address_coin}'])
                usd_value = price * amount_coin
                print(f'{amount_coin} {name_coin} = {usd_value:3f} usd')
                sum_usd += usd_value
                dict_tokens[name_coin] = usd_value
            except KeyError as e:
                print(f'Нет цены для {amount_coin} {name_coin}')

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
