#!/usr/bin/python3

import requests, json, os
# import telebot

dirAtivos = 'C:/Users/jp/Desktop/scrape/ativos.txt'
dirValores = 'C:/Users/jp/Desktop/scrape/valores.txt'
# dirBot = 'C:/Users/jp/Desktop/scrape/bot.txt' # Token do bot p/ Telegram (BotFather)
dirApi = 'C:/Users/jp/Desktop/scrape/api.txt' # Token do api do WorldTradingData

site = 'https://api.worldtradingdata.com/api/v1/stock?symbol='

# with open(dirBot, 'r') as f:
#     token_bot = f.read()
#     bot = telebot.TeleBot(token_bot)

with open(dirApi, 'r') as f:
    token_api = f.read()

with open(dirAtivos, 'r') as f:
    inp = f.read()
    ativos = inp.split(',')
    print('Ativos =', ativos)

url = site + inp + token_api

data = requests.get(url).json()
n = data['symbols_returned']
list_p = []

for i in range(0, n, 1):
    nomes = data['data'][i]['symbol']
    preco = data['data'][i]['price']
    list_p.append(preco)
    # list.append((nomes, preco))
print('\nValores =', list_p)

out = []
for j in range(0, n, 1):
    v = ativos[j].replace('.SA', '') + ' ' + list_p[j]
    out.append(v)
print('\nLista =', out, '\n')

with open(dirValores, 'w') as f:
    f.write('\n'.join(map(str, out)))

os.system('pause')
