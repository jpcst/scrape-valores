#!/usr/bin/python3

import scpr3
import requests

dirId = '/home/jpcst/scrape-valores/id.txt'
dirBot = '/home/jpcst/scrape-valores/bot.txt'

with open(dirBot, 'r') as f, open(dirId, 'r') as g:
    api_bot = f.read()
    chat_id = g.read()

v = scpr3.main()

list = '——————————\n' + \
        (','.join(map(str,v))).replace(',','\n') + \
        '\n——————————'

url = 'https://api.telegram.org/bot'+ api_bot + '/sendMessage?chat_id=' + chat_id + '&text=' + list
go = requests.post(url)


