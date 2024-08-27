from check_wallets import WalletCoins
from open_txt import my_wallets
from check_wallets import Coin

for wallet in my_wallets:
    # каждую итерацию создаём объект класса WalletCoins c новым адресом кошелька 'wallet'
    my_wallet_coins = WalletCoins(wallet)

    # вызываем чеккер монет кошелька для созданного объекта
    my_wallet_coins.check_tokens()

    # вызываем чеккер NFT кошелька для того же объекта
    my_wallet_coins.check_nft()
