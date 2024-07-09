import requests
from open_txt import api_key


class WalletCoins:
    # получаем список и количество монет в кошельке
    def __init__(self, wallet, limit=25):
        self.wallet = wallet
        self.limit = limit
        self._api_key = api_key
        self.url = "https://mainnet-aptos-api.moralis.io/wallets/coins"
        self.headers = {"accept": "application/json", "X-API-Key": self._api_key}
        self.params = {"limit": limit, "owner_addresses[0]": self.wallet}
        self.response = requests.get(url=self.url, headers=self.headers, params=self.params).json()

    def check_coins(self):
        # проверяем ответ сервера
        try:
            self.response = requests.get(url=self.url, headers=self.headers, params=self.params).json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API в check_coins: {e}")
            self.response = {'result': []}

        print(f'в кошельке {self.wallet}:')

        for coin in self.response['result']:
            index_coin = coin['coin_type'].rfind('::')
            print(f'{int(coin['amount']) / 10000000} {coin['coin_type'][index_coin + 2:]}')


class WalletNft(WalletCoins):
    def __init__(self, wallet):
        super().__init__(wallet)
        self.url = "https://mainnet-aptos-api.moralis.io/wallets/nfts"

    def check_nft(self):
        # проверяем ответ сервера
        try:
            self.response = requests.get(url=self.url, headers=self.headers, params=self.params).json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API в check_nft: {e}")

        count_nft = 0
        for nft in self.response['result']:
            print(f'{nft["collection_name"]}')
            count_nft += 1
        print(f'в кошельке {self.wallet}: {count_nft} NFT')
