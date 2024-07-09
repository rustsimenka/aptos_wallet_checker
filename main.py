from check_wallet import WalletNft, WalletCoins
from open_txt import my_wallets


for wallet in my_wallets:
    my_wallet_nft = WalletNft(wallet)
    my_wallet_nft.check_nft()
    my_wallet = WalletCoins(wallet)
    my_wallet.check_coins()