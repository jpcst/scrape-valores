#!/usr/bin/python3

import scpr3
import telebot

dirId = 'C:/Users/jp/Desktop/scrape/id.txt'
dirBot = 'C:/Users/jp/Desktop/scrape/bot.txt'

with open(dirBot, 'r') as f, open(dirId, 'r') as g:
    api_bot = f.read()
    chatId = g.read()

tb = telebot.TeleBot(api_bot)

def telegram():
    tb.send_message(chatId, list)

v = scpr3.main()

list = '——————————\n' + \
        (','.join(map(str,v))).replace(',','\n') + \
        '\n——————————'

telegram()
