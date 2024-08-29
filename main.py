from check_wallets import AllTokensInWallet
from open_txt import my_wallets
from coin_price import CoinPrice
from check_wallets import print_coins_value_usd
from check_wallets import count_nft
import datetime


def iterate_my_wallets() -> str:
    for wallet in my_wallets:
        # каждую итерацию создаём объект класса со следующим адресом кошелька из списка
        my_wallet_coins = AllTokensInWallet(wallet)
        print(f'в кошельке {wallet} на {datetime.date.today()}:', end='\n')

        # вызываем функцию подсчёта стоимости монет для экземпляра класса:
        print_coins_value_usd(my_wallet_coins.check_all_coins_amount())
        dict_nft = count_nft(my_wallet_coins.check_all_nft_amount())  # создаём словарь с именами и количеством НФТ
        total_nfts = sum(dict_nft.values())  # считаем сумму всех НФТ по значениям ключей
        print(f'всего в кошельке {wallet} - {total_nfts} NFT:', end='\n')
        print(*dict_nft.items(), sep='\n')


iterate_my_wallets()
