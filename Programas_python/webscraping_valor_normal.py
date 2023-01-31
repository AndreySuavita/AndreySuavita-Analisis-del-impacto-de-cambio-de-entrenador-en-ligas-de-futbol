from bs4 import BeautifulSoup
import requests
import pandas as pd

lista_arreglar_resultado=[]
for x in list(range(0, 30)):
    for y in list(range(0, 30)):
        lista_arreglar_resultado.append(' ' + '(' + str(x) + ':' + str(y) + ')')

lista_arreglar_resultado.append('3:2 (1:1, 1:1) pn.')
lista_arreglar_resultado.append('7:6 (0:0, 0:0) pn.')
## para finales
url='https://www.livefutbol.com/calendario/col-primera-a-2020-liguilla-de-eliminados-halbfinale/0/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser' )
eq = soup.find_all('div',class_='data')

#print(len(eq[2].table.find_all('tr')))
#print(eq[2].table.find_all('tr')[3])
#print(len(eq[2].table.find_all('tr')[3].find_all('td')))
#print(eq[2].table.find_all('tr')[3].find_all('td'))
jornada_lista=[]
local=[]
visitante=[]
goles_local=[]
goles_visitante=[]
fecha=[]

for x in (eq[2].table.find_all('tr')):
    tag = x.find_all('td')
    jornada_lista.append("semifinal")
    for y in list(range(0, 7)):
        # fecha
        if y == 0:
            z = tag[y].text
            z = z.replace('\n', '')
            z = z.replace('.', '-')
            fecha.append(z)
        # local
        elif y == 2:
            z = tag[y].text
            z = z.replace('\n', '')
            local.append(z)
        # visitante
        elif y == 4:
            z = tag[y].text
            z = z.replace('\n', '')
            visitante.append(z)
        # goles
        elif y == 5:
            z = tag[y].text
            z = z.replace('\n', '')
            print('###########')
            print(z)
            # for para quitar los resultados de medio tiempo
            for posibilidad in lista_arreglar_resultado:
                z = z.replace(posibilidad, '')
            print(z + 'h')
            print(len(eq[1].find_all('form')[1].find_all('option')))
#            print(url_iterada)
            z_lista = z.split(':')
            if (z == '-:- ' or z == ' -:- ' or z == ' no jug. '  or z == ' no jug.' or z == ' apla.' or z == 'apla. '):
                goles_local.append(None)
                goles_visitante.append(None)
            else:
                goles_local.append(int(float(z_lista[0])))
                goles_visitante.append(int(float(z_lista[1])))
            # print(len(goles_local))
            print(len(goles_visitante))
        else:
            continue
print(local,visitante,goles_local,goles_visitante,fecha)
