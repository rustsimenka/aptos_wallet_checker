from check_wallets import WalletCoins, WalletNfts
from open_txt import my_wallets
from pprint import pprint


for wallet in my_wallets:
    my_wallet_coins = WalletCoins(wallet)
    my_wallet_coins.check_token()
    print('-----------------')
    my_wallet_nft = WalletNfts(wallet)

    my_wallet_nft.check_nft()




