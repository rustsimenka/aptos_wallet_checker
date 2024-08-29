import requests
from coin_price import CoinPrice
from open_txt import api_key
from pprint import pprint


class AllTokensInWallet:
    # получаем количество монет и НФТ в кошельке
    def __init__(self, wallet, limit=25):
        self.wallet = wallet
        self.limit = limit
        self._api_key = api_key
        self.headers = {"accept": "application/json", "X-API-Key": self._api_key}
        self.params = {"limit": limit, "owner_addresses[0]": self.wallet}
        self.url_coins = "https://mainnet-aptos-api.moralis.io/wallets/coins"
        self.url_nft = "https://mainnet-aptos-api.moralis.io/wallets/nfts"

    def check_all_coins_amount(self) -> dict:
        dict_all_coins = requests.get(url=self.url_coins, headers=self.headers, params=self.params).json()
        return dict_all_coins['result']

    def check_all_nft_amount(self):
        dict_all_nft = requests.get(url=self.url_nft, headers=self.headers, params=self.params).json()
        return dict_all_nft['result']


def print_coins_value_usd(dict_coins_from_wallet) -> float:
    dict_coins = {}
    for coin in dict_coins_from_wallet:
        coin_class = CoinPrice(coin)
        if coin_class.usd_value > 0:
            print(f'{coin_class.amount_coin} {coin_class.name_coin} = {coin_class.usd_value:3f} usd')
        else:
            print(f'Нет цены для {coin_class.amount_coin} {coin_class.name_coin}')

        dict_coins[coin_class.name_coin] = coin_class.usd_value
        total_sum_coins = float(sum(dict_coins.values()))

    print(f'Итого в кошельке монет на сумму {round(total_sum_coins, 3)} USD')


def count_nft(dict_nft_from_wallet) -> dict:
    dict_nft = {}
    for token in dict_nft_from_wallet:
        name_nft = token["collection_name"]
        if "collection_name" in token:
            if name_nft not in dict_nft_from_wallet:
                dict_nft[name_nft] = 1
            else:
                dict_nft[name_nft] += 1
    return dict_nft
