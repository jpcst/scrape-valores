#!/usr/bin/python3

def main():

    #from os import system
    from math import ceil, floor
    import requests
    import json
    import numpy as np

    dirAtivos = '/home/jpcst/scrape-valores/ativos.txt'
    dirValores = '/home/jpcst/scrape-valores/valores.txt'
    dirApi = '/home/jpcst/scrape-valores/api.txt'
    dirIni = '/home/jpcst/scrape-valores/inicio.txt'
    dir_start = '/home/jpcst/scrape-valores/start.txt'
    site = 'https://api.worldtradingdata.com/api/v1/stock?symbol='

    def scrape(lista):

        listIte = (','.join(map(str,lista)))
        url = site + listIte + token_api
        data = requests.get(url).json()
        n = data['symbols_returned'] # Numero de valores retornados pelo site
        list_p = []
        list_n = []
        for i in range(0, n, 1): # Loopa n vezes
            preco = data['data'][i]['price'] # Scrapa os valores
            name = data['data'][i]['symbol'] # Scrapa os nomes
            list_p.append(preco)
            list_n.append(name)
        print('\nValores =', list_p)

        out = []  # Lista final
        
        with open(dirIni, 'r') as  f:
            inicio = f.read()
            list_i = inicio.split(',')

        list_i = [float(i) for i in list_i] # Inicial
        list_p_float = [float(i) for i in list_p] # Final
        
        with open(dir_start, 'r') as f:
            list_start = f.read().split(',')
        list_start = [float(i) for i in list_start]
        print(list_start) # Lista dos valores pago na compra
        
        list_end = []
        for i in range(len(list_start)):
            venda = list_start[i]*list_p_float[i]/list_i[i]
            list_end.append(venda)
        print(list_end) # Lista dos valores na hora da venda
        
        dif = []
        for i in range(len(list_i)):
            dif.append(round((list_p_float[i]/list_i[i] - 1) * 100, 2))
            #dif.append(round(list_p_float[i]/list_i[i] * 100 - 100, 2))
        dif = [str(i) for i in dif]
        for i in range(0, n, 1):
            # v = ativos[i].replace('.SA', '') + ' ' + list_p[i]  # Ativos e valores
            # v = list_p[i]
            v = list_n[i] + ' ' + list_p[i] + ' (' + dif[i] + '%)'
            # v = ativos[i] + ' ' + list_p[i]
            out.append(v)  # Lista final
        print('Lista =', out)

        h.writelines('\n'.join(map(str, out)) + '\n') # Salva no txt

        return out

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
                v = scrape(list[i])
        else:
            v = scrape(ativos)

    print('')
    #system('pause')
    return v

if __name__ == '__main__':
    main()
