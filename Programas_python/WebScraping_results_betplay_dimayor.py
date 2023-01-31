from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.livefutbol.com/calendario/col-primera-a-2022-clausura-spieltag/20/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
eq = soup.find_all('div', class_='data')

fecha = []
jornada_lista = []
local = []
visitante = []
goles_local = []
goles_visitante = []

# crear listas para arreglar resultados

lista_arreglar_resultado = []
lista_posibles_resultados = list(range(0, 20))

for x in list(range(0, 30)):
    for y in list(range(0, 30)):
        lista_arreglar_resultado.append(' ' + '(' + str(x) + ':' + str(y) + ')')
lista_arreglar_resultado.append(' (0:1, 2:1) ')
# con estos print se buscan los años y jornadas de la pagina
# print(len(eq[1].find_all('form')[1].find_all('option')))
# print(eq[1].find_all('form')[0].find_all('option')[0].text)
# print(eq[1].find_all('form')[1].find_all('option')[0].text)


url_principal = 'https://www.livefutbol.com/calendario/col-primera-a-'
for años in (eq[1].find_all('form')[0].find_all('option')):
    añosarreglados = años.text
    añosarreglados = añosarreglados.replace('/', '-')
    añosarreglados = añosarreglados.replace(' ', '-')
    # recordar cambiar en los links el "/" por "-"
    if (añosarreglados in ['2022-Apertura-Playoffs','2021-Clausura-Playoffs','2021-Apertura-Playoffs','2020-Playoffs','2020-Liguilla-de-Eliminados','2020-Copa-Sud-Playoff',
                           '2019-Clausura-Playoffs','2019-Apertura-Playoffs','2018-Clausura-Playoffs','2018-Apertura-Playoffs','2017-Clausura-Playoffs','2017-Apertura-Playoffs',
                           '2016-Clausura-Playoffs','2016-Apertura-Playoffs','2015-Clausura-Playoffs','2015-Apertura-Playoffs','2014-Clausura-Playoffs','2014-Apertura-Playoffs',
                           '2013-Clausura-Playoffs','2013-Apertura-Playoffs','2012-Clausura-Playoffs','2012-Apertura-Playoffs','2011-Clausura-Playoffs','2011-Apertura-Playoffs',
                           '2010-Clausura-Playoffs','2010-Apertura-Playoffs','2009-Clausura-Playoffs','2009-Apertura-Playoffs','2008-Clausura-Cuadrangulares','2008-Apertura-Cuadrangulares',
                           '2007-Clausura-Cuadrangulares','2007-Apertura-Cuadrangulares']):
        continue
    elif (añosarreglados == '2020'):
        url_iterada = 'https://www.livefutbol.com/calendario/col-primera-a-2020-apertura-spieltag/'
    elif (añosarreglados == '2009-Apertura'):
        url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2009-apertura-spieltag/'
    elif (añosarreglados == '2009-Clausura'):
        url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2009-clausura-spieltag/'
    elif (añosarreglados == '2008-Clausura'):
        url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2008-clausura-spieltag/'
    elif (añosarreglados == '2008-Apertura'):
        url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2008-apertura-spieltag/'
    elif (añosarreglados == '2007-Clausura'):
        url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2007-clausura-spieltag/'
    elif (añosarreglados == '2007-Apertura'):
        url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2007-apertura-spieltag/'
    else:
        url_iterada = url_principal + añosarreglados + '-spieltag/'
    print('primerfor ' + url_iterada)
    page = requests.get(url_iterada)
    soup = BeautifulSoup(page.content, 'html.parser')
    eq = soup.find_all('div', class_='data')
    for jornada in list(range(len(eq[1].find_all('form')[1].find_all('option'))-1,-1,-1)):
        if (eq[1].find_all('form')[1].find_all('option')[jornada]) in ["Final","Semifinales","Cuartos de final","Grupo A","Grupo B","Final"]:
            continue
        else:
            jornada_actual = eq[1].find_all('form')[1].find_all('option')[jornada].text
            jornada_numero = jornada_actual.split('.')
            añosarreglados = años.text
            añosarreglados = añosarreglados.replace('/', '-')
            añosarreglados = añosarreglados.replace(' ', '-')
            # recordar cambiar en los links el "/" por "-"
            if (añosarreglados == '2020'):
                url_iterada = 'https://www.livefutbol.com/calendario/col-primera-a-2020-apertura-spieltag/'+jornada_numero[0]+'/'
            elif (añosarreglados == '2009-Apertura'):
                url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2009-apertura-spieltag/'+jornada_numero[0]+'/'
            elif (añosarreglados == '2009-Clausura'):
                url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2009-clausura-spieltag/'+jornada_numero[0]+'/'
            elif (añosarreglados == '2008-Clausura'):
                url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2008-clausura-spieltag/'+jornada_numero[0]+'/'
            elif (añosarreglados == '2008-Apertura'):
                url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2008-apertura-spieltag/'+jornada_numero[0]+'/'
            elif (añosarreglados == '2007-Clausura'):
                url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2007-clausura-spieltag/'+jornada_numero[0]+'/'
            elif (añosarreglados == '2007-Apertura'):
                url_iterada = 'https://www.livefutbol.com/calendario/col-copa-mustang-2007-apertura-spieltag/'+jornada_numero[0]+'/'
            else:
                url_iterada = url_principal + añosarreglados + '-spieltag/'+jornada_numero[0]+'/'

            print('segundofor ' + url_iterada)
            # print(url_iterada)

            page = requests.get(url_iterada)
            soup = BeautifulSoup(page.content, 'html.parser')
            eq = soup.find_all('div', class_='data')

            ##########################################################

            for x in (eq[2].table.find_all('tr')):
                tag = x.find_all('td')
                jornada_lista.append(int(float(jornada_numero[0])))
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
                        print(url_iterada)
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
                        # print(tag[y].text)

# con esto print se seleccionan los datos de la pagina
# print(eq[2].table.find_all('tr')[0].find_all('td')[0].text) #0,2,4,5
# print(eq[2].table.find_all('tr'))
# print(len(eq[2].table.find_all('tr')))

# print(fecha,local,visitante,resultado)
# print(len(fecha),len(local),len(visitante),len(resultado))

df = pd.DataFrame(
    {'fecha': fecha, 'jornada': jornada_lista, 'local': local, 'visitante': visitante, 'goles_local': goles_local,
     'goles_visitante': goles_visitante})

# trasnformar en datatime las columnas respectivas
# df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')

df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/betplay_dimayor_results', index=False)
print(df)