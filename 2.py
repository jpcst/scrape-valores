#!/usr/bin/python3

import requests
import json
from os import system
# import telebot
import schedule, time

dirAtivos = 'C:/Users/jp/Desktop/scrape/ativos.txt'
dirValores = 'C:/Users/jp/Desktop/scrape/valores.txt'
# dirBot = 'C:/Users/jp/Desktop/scrape/bot.txt' # Token do bot p/ Telegram (BotFather)
dirApi = 'C:/Users/jp/Desktop/scrape/api.txt'  # Token do api do WorldTradingData
site = 'https://api.worldtradingdata.com/api/v1/stock?symbol='
# chatId = ''

# with open(dirBot, 'r') as f:
#    token_bot = f.read()
# tb = telebot.TeleBot(token_bot)

with open(dirApi, 'r') as f:
    token_api = f.read()

with open(dirAtivos, 'r') as f:
    inp = f.read()  # Input de ativos do user no .txt
    ativos = inp.split(',')  # Lista de ativos
    print('Ativos =', ativos)

url = site + inp + token_api

data = requests.get(url).json()
n = data['symbols_returned']
list_p = []

for i in range(0, n, 1):  # Loopa n vezes, n = número de valores retornados pela api
    preco = data['data'][i]['price']  # Scrapa todos os preços
    list_p.append(preco)  # Lista de preços
print('Valores =', list_p)

out = []  # Lista final => ['ATIVO' 'VALOR']
for j in range(0, n, 1):
    v = ativos[j].replace('.SA', '') + ' ' + list_p[j]  # Ativos e valores
    # v = ativos[j] + ' ' + list_p[j]
    out.append(v)  # Lista final
print('\nLista =', out, '\n')

with open(dirValores, 'w') as f:
    f.write('\n'.join(map(str, out)))  # Salva a lista final no .txt

#def telegram():
   # for i in range(len(ativos)):
  #      tb.send_message(chatId, out[i])
 #   tb.polling(timeout=0)

#telegram()

# schedule.every(1).minutes.do(telegram)
# while True:
    # schedule.run_pending()
    # time.sleep(1)

system('pause')
