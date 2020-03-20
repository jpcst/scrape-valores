#!/usr/bin/python3

from os import system
from math import ceil
import requests
import json

# Declaração das variáveis
dir_ativos = 'C:/SCPR/inputs/ativos.txt' # Lista dos ativos DEVEM estar em ordem alfabética com '.SA' no final e separados por vírgula. Ex: BOVA11.SA,CVCB3.SA,WEGE3.SA
dir_valores = 'C:/SCPR/inputs/valores.txt' # Aqui será salvo o output final
dir_api = 'C:/SCPR/inputs/constantes/api.txt' # Escrever nesse formato: &api_token=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
dir_bot = 'C:/SCPR/inputs/constantes/bot.txt' # Token do bot no BotFather
dir_id = 'C:/SCPR/inputs/constantes/id.txt' # Seu ID no telegram p/ o bot mandar a msg. Chamar @chatid_echo_bot no app
site = 'https://api.worldtradingdata.com/api/v1/stock?symbol='

dir_pago = 'C:/SCPR/inputs/constantes/pago.txt'
dir_inicial = 'C:/SCPR/inputs/constantes/inicial.txt'

######################################################

with open(dir_pago) as f:
    pago = f.read().replace('\n','').split(',')
    pago = [float(i) for i in pago]

with open(dir_inicial) as f:
    inicial = f.read().replace('\n','').split(',')
    inicial = [float(i) for i in inicial]

######################################################

# Leitura dos arquivos
with open(dir_api, 'r') as f:
    token_api = f.read()
with open(dir_ativos, 'r') as f:
    ativos = f.read().replace('\n','').split(',')
with open(dir_bot, 'r') as f:
    api_bot = f.read()
with open(dir_id, 'r') as f:
    chat_id = f.read()

def telegram(lista): # Enviar msg
    msg = '————————————————————\n' + \
    		(','.join(map(str,lista))).replace(',','\n') + \
    		'\n————————————————————'
    url = 'https://api.telegram.org/bot' + api_bot + '/sendMessage?chat_id=' + chat_id + '&text=' + msg # Api do telegram
    requests.post(url) # Enviar

def scrape(lista): # Busca os valores dos ativos
    list = (','.join(map(str,lista))) # Pega o input da func. e formata corretamente para que a pesquisa funcione
    url = site + list + token_api
    data = requests.get(url).json()
    n = data['symbols_returned'] # Número de valores retornados pelo site
    list_p = [] # Lista para armazenar os preços
    list_n = [] # Lista para armazenar os nomes
    out = [] # Lista final
    perc = [] # Ganho ou perca percentual
    dif = [] # Valor dos ativos hoje

    for i in range(n):
        preco = data['data'][i]['price'] # Valores
        name = data['data'][i]['symbol'] # Nomes
        list_p.append(preco)
        list_n.append(name)
        list_p = [float(x) for x in list_p]

        lp = (list_p[i] / inicial[i] - 1) * 100
        perc.append(round(lp, 2))

        agora = pago[i] * list_p[i] / inicial[i]
        dif.append(round(agora, 2))

        v = '{} {} ({}%) L/P {}'.format(list_n[i], list_p[i], perc[i], round(float(dif[i]) - float(pago[i])), 4)
        out.append(v)

    print(dif)
    print(perc)
    print('Ativos: ', list_n)
    print('Valores: ', list_p)
    print('Output: ', out, '\n')
    return out

m = len(ativos)
if m > 5: # Só é possível buscar 5 ativos por vez com a API gratuita, então se a lista é maior que 5, é necessário iterar x vezes
    print('Iterações: ', ceil(m/5), '\n')
    lista_nova = []
    for i in range(0, m, 5):
        lista_nova.append(ativos[i:i+5]) # A cada 5 ativos é criado uma lista deles dentro de lista_nova
    for i in range(len(lista_nova)):
        v = scrape(lista_nova[i])
        telegram(v) # Envia a msg
        if i == 0:
            with open(dir_valores, 'w') as f: # Salva o output em um .txt
                f.write('\n'.join(map(str, v)))
                f.write('\n')
        else:
            with open(dir_valores, 'a') as f:
                f.write('\n'.join(map(str, v)))
                f.write('\n')

else:
    v = scrape(ativos)
    telegram(v) # Envia a msg
    with open(dir_valores, 'w') as f: # Salva o output em um .txt
        f.write('\n'.join(map(str, v)))

system('pause')
