# Читаем API ключ из файла
with open('my_api.txt') as my_api_file:
    api_key = my_api_file.read().strip()

# Читаем все кошельки из файла и сохраняем их в список
with open('wallets.txt') as my_wallets:
    my_wallets = [line.strip() for line in my_wallets]
