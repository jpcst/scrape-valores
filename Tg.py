#!/usr/bin/python3

import scpr3
import telebot
import schedule

dirId = 'C:/Users/jp/Desktop/scrape/id.txt'
dirBot = 'C:/Users/jp/Desktop/scrape/bot.txt'

with open(dirBot, 'r') as f, open(dirId, 'r') as g:
    api_bot = f.read()
    chatId = g.read()

tb = telebot.TeleBot(api_bot)

def telegram():
    tb.send_message(chatId, list)

schedule.every().day.at("03:08").do(telegram)


v = scpr3.main()

list = '——————————\n' + \
        (','.join(map(str,v))).replace(',','\n') + \
        '\n——————————'

telegram()
