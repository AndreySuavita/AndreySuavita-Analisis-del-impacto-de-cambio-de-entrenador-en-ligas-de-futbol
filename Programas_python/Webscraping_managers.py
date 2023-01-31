from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.livefutbol.com/equipos/Manchester-United/9/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser' )
eq = soup.find_all('div',class_='data')
#tiempo_activo = eq[0].text
#entrenador = eq[1].text
#pais = eq[2].img.get('title')
#tres = eq[3]
#cuarto = eq[4]

#print(eq[2].img.get('title'))

fecha_activo_inicio = []
fecha_activo_fin = []
entrenador = []
pais = []
fecha_nacimiento = []
contador=False

for x in (eq[1].table.find_all('tr')):
    if contador!=False:
        tag = x.find_all('td')
        for y in list(range(0,4)):
            if y == 0:
#               tiempo_activo.append(tag[y].text)
                fecha_completa = tag[y].text
                lista_fecha_completa = fecha_completa.split(' - ')
                fecha_inicio = lista_fecha_completa[0].replace('.','-')
                fecha_fin = lista_fecha_completa[1].replace('.','-')
                fecha_activo_inicio.append(fecha_inicio)
                fecha_activo_fin.append(fecha_fin)

            elif y == 1:
                entrenador.append(tag[y].text)
            elif y == 2:
                pais.append(tag[y].img.get('title'))
            else:
#                fecha_nacimiento.append(tag[y].text)
                fecha_nacimiento_ = tag[y].text
                fecha_nacimiento_ = fecha_nacimiento_.replace('.','-')
                fecha_nacimiento.append(fecha_nacimiento_)

    else:
        contador=True

df = pd.DataFrame({'fecha_activo_inicio':fecha_activo_inicio,'fecha_activo_fin':fecha_activo_fin,'entrenador':entrenador,'pais':pais,'fecha_nacimiento':fecha_nacimiento})

# con esto print se seleccionan los datos de la pagina
#print(eq[1].table.find_all('tr')[22].find_all('td')[2].img.get('title'))
#print(len(eq[1].table.find_all('tr')))

#trasnformar en datatime las columnas respectivas

print(df.info())
#df['fecha_activo_inicio'] = pd.to_datetime(df['fecha_activo_inicio'], errors='coerce')
#df['fecha_activo_fin'] = pd.to_datetime(df['fecha_activo_fin'], errors='coerce')
#df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], errors='coerce')
print(df.info())
print(df)

#guardar dataframe sin indice
#df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/premier_league/Manchester United_premier_league',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)