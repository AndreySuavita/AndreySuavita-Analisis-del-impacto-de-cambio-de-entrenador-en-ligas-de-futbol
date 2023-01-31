from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.livefutbol.com/calendario/ned-eredivisie-2021-2022-spieltag/34/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser' )
eq = soup.find_all('div',class_='data')

fecha=[]
jornada_lista=[]
local=[]
visitante=[]
goles_local=[]
goles_visitante=[]

#crear listas para arreglar resultados

lista_arreglar_resultado = []
lista_posibles_resultados = list(range(0,20))

for x in list(range(0,30)):
    for y in list(range(0,30)):

        lista_arreglar_resultado.append(' '+'('+str(x)+':'+str(y)+')')


# con estos print se buscan los años y jornadas de la pagina
#print(len(eq[1].find_all('form')[1].find_all('option')))
#print(eq[1].find_all('form')[0].find_all('option')[0].text)
#print(eq[1].find_all('form')[1].find_all('option')[0].text)


url_principal='https://www.livefutbol.com/calendario/ned-eredivisie-'
for años in (eq[1].find_all('form')[0].find_all('option')):
    añosarreglados = años.text
    añosarreglados = añosarreglados.replace('/', '-')
    #recordar cambiar en los links el "/" por "-"
    if (añosarreglados == '2022-2023'):
        continue
    else:
        url_iterada = url_principal + añosarreglados + '/'
    print('primerfor ' + url_iterada)
    page = requests.get(url_iterada)
    soup = BeautifulSoup(page.content, 'html.parser')
    eq = soup.find_all('div', class_='data')
    for jornada in list(range(len(eq[1].find_all('form')[1].find_all('option'))-1,-1,-1)):
        jornada_actual = eq[1].find_all('form')[1].find_all('option')[jornada].text
        jornada_numero=jornada_actual.split('.')
        añosarreglados=años.text
        añosarreglados=añosarreglados.replace('/','-')
        url_iterada=url_principal+añosarreglados+'-spieltag/'+jornada_numero[0]+'/'
        print('segundofor ' + url_iterada)
        #print(url_iterada)
        
        page = requests.get(url_iterada)
        soup = BeautifulSoup(page.content, 'html.parser')
        eq = soup.find_all('div', class_='data')

        ##########################################################

        for x in (eq[2].table.find_all('tr')):
            tag = x.find_all('td')
            jornada_lista.append(int(float(jornada_numero[0])))
            for y in list(range(0, 7)):
                #fecha
                if y == 0:
                    z = tag[y].text
                    z = z.replace('\n', '')
                    z = z.replace('.', '-')
                    fecha.append(z)
                #local
                elif y == 2:
                    z = tag[y].text
                    z = z.replace('\n', '')
                    local.append(z)
                #visitante
                elif y == 4:
                    z = tag[y].text
                    z = z.replace('\n', '')
                    visitante.append(z)
                #goles
                elif y == 5:
                    z = tag[y].text
                    z = z.replace('\n', '')
                    print('###########')
                    print(z)
                    #for para quitar los resultados de medio tiempo
                    for posibilidad in lista_arreglar_resultado:
                        z = z.replace(posibilidad,'')
                    print(z+'h')
                    print(len(eq[1].find_all('form')[1].find_all('option')))
                    print(url_iterada)
                    z_lista=z.split(':')
                    if (z=='-:- ' or  z==' no jug.'):
                        goles_local.append(None)
                        goles_visitante.append(None)
                    else:
                        goles_local.append(int(float(z_lista[0])))
                        goles_visitante.append(int(float(z_lista[1])))
                    #print(len(goles_local))
                    print(len(goles_visitante))
                else:
                    continue
                    #print(tag[y].text)


# con esto print se seleccionan los datos de la pagina
#print(eq[2].table.find_all('tr')[0].find_all('td')[0].text) #0,2,4,5
#print(eq[2].table.find_all('tr'))
#print(len(eq[2].table.find_all('tr')))

#print(fecha,local,visitante,resultado)
#print(len(fecha),len(local),len(visitante),len(resultado))

df = pd.DataFrame({'fecha':fecha,'jornada':jornada_lista,'local':local,'visitante':visitante,'goles_local':goles_local,'goles_visitante':goles_visitante})

#trasnformar en datatime las columnas respectivas
#df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')

df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/eredivisie_paises_bajos_results',index=False)
print(df)
