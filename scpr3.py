#!/usr/bin/python3

# from os import system
from math import ceil, floor
import requests
import json

dirAtivos = 'C:/Users/jp/Desktop/scrape/ativos.txt'
dirValores = 'C:/Users/jp/Desktop/scrape/valores.txt'
dirApi = 'C:/Users/jp/Desktop/scrape/api.txt'
site = 'https://api.worldtradingdata.com/api/v1/stock?symbol='

def scrape(lista):

    listIte = (','.join(map(str,lista)))
    url = site + listIte + token_api
    data = requests.get(url).json()
    n = data['symbols_returned'] # Numero de valores retornados pelo site
    list_p = []
    for i in range(0, n, 1): # Loopa n vezes
        preco = data['data'][i]['price'] # Scrapa os valores
        list_p.append(preco)
    print('\nValores =', list_p)

    out = []  # Lista final
    for i in range(0, n, 1):
        # v = ativos[i].replace('.SA', '') + ' ' + list_p[i]  # Ativos e valores
        # v = list_p[i]
        v = lista[i] + ' ' + list_p[i]
        # v = ativos[i] + ' ' + list_p[i]
        out.append(v)  # Lista final
    print('Lista =', out)

    h.writelines('\n'.join(map(str, out)) + '\n') # Salva no txt

with open(dirAtivos, 'r') as f, open(dirApi, 'r') as g, open(dirValores, 'w') as h:
    token_api = g.read()
    inp = f.read().replace('\n','')
    ativos = inp.split(',')

    print('Ativos =', ativos, '\n')
    m = len(ativos)

    if (m > 5):
        iter = ceil(m/5)
        print('Iterações:',iter)
        #totI = iter * 5
        #listaVazia = 5 - (totI - m)
        listaCheia = floor(m/5)
        resto = m % 5

        list = [[0]*5 for i in range(listaCheia+1)]
        i=z=0
        listaCheia +=1
        while i < listaCheia:
            j=0
            while j < 5:
                list[i][j] = ativos[z]
                j = j+1
                z = z+1
                if z==m:
                    break
            i +=1

        for i in range(len(list)):
            scrape(list[i])
    else:
        scrape(ativos)

print('')
# system('pause')
