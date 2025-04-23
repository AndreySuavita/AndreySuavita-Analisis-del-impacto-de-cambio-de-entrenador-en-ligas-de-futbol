from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Barcelona', 'Atlético', 'SD Eibar', 'Levante',
       'Sporting de Huelva', 'CD Alavés', 'Real Sociedad', 'Madrid CFF',
       'Real Betis', 'Sevilla', 'Villarreal CF', 'Valencia', 'Athletic',
       'Rayo', 'Real Madrid', 'UDG Tenerife Sur', 'EDF Logroño',
       'Espanyol', 'Santa Teresa CD', 'Deportivo de La Coruña',
       'CD Tacón', 'Málaga CF', 'Fundación Albacete', 'Zaragoza CFF',
       'Oiartzun ', 'UD Tacuense', 'Oviedo Moderno CF',
       'Transportes Alcaine', 'UD Collerense', 'CE Sant Gabriel',
       'Levante Las Planas', 'Granada']
equipos_fc=['Real-Sociedad']
club=[]
fecha_activo_inicio = []
fecha_activo_fin = []
entrenador = []
pais = []
fecha_nacimiento = []
contador=False

for equipo in equipos:
    contador=False
    equipo_1 = equipo.replace(' ','-')
    if (equipo_1 in equipos_fc):
        equipo_1 = equipo_1+'-frauen'
    elif (equipo_1 == 'Barcelona'):
        equipo_1 = 'fc-barcelona-frauen'
    elif (equipo_1 == 'Atlético'):
        equipo_1 = 'atletico-madrid-frauen'
    elif (equipo_1 == 'SD-Eibar'):
        equipo_1 = 'SD-Eibar-frauen'
    elif (equipo_1 == 'Levante'):
        equipo_1 = 'levante-ud-frauen'
    elif (equipo_1 == 'Sporting-de-Huelva'):
        equipo_1 = 'sporting-de-huelva-frauen'
    elif (equipo_1 == 'CD-Alavés'):
        equipo_1 = 'cd-alaves-frauen'
    elif (equipo_1 == 'Madrid-CFF'):
        equipo_1 = 'madrid-cff-frauen'
    elif (equipo_1 == 'Real-Betis'):
        equipo_1 = 'real-betis-frauen'
    elif (equipo_1 == 'Sevilla'):
        equipo_1 = 'sevilla-fc-frauen'
    elif (equipo_1 == 'Villarreal-CF'):
        equipo_1 = 'villarreal-cf-frauen'
    elif (equipo_1 == 'Valencia'):
        equipo_1 = 'valencia-cf-frauen'
    elif (equipo_1 == 'Athletic'):
        equipo_1 = 'athletic-bilbao-frauen'
    elif (equipo_1 == 'Rayo'):
        equipo_1 = 'rayo-vallecano-frauen'
    elif (equipo_1 == 'Real-Madrid'):
        equipo_1 = 'real-madrid-frauen'
    elif (equipo_1 == 'UDG-Tenerife-Sur'):
        equipo_1 = 'udg-tenerife-sur-frauen'
    elif (equipo_1 == 'EDF-Logroño'):
        equipo_1 = 'edf-logrono-frauen'
    elif (equipo_1 == 'Espanyol'):
        equipo_1 = 'espanyol-barcelona-frauen'
    elif (equipo_1 == 'Santa-Teresa-CD'):
        equipo_1 = 'santa-teresa-cd-frauen'
    elif (equipo_1 == 'CD-Tacón'):
        equipo_1 = 'real-madrid-frauen'
    elif (equipo_1 == 'Deportivo-de-La-Coruña'):
        equipo_1 = 'deportivo-de-la-coruna-frauen'
    elif (equipo_1 == 'Málaga-CF'):
        continue
    elif (equipo_1 == 'Deportivo-de-La-Coruña'):
        equipo_1 = 'deportivo-de-la-coruna-frauen'
    elif (equipo_1 == 'Fundación-Albacete'):
        continue
    elif (equipo_1 == 'Zaragoza-CFF'):
        continue
    elif (equipo_1 == 'Oiartzun-'):
        continue
    elif (equipo_1 == 'UD-Tacuense'):
        continue
    elif (equipo_1 == 'Oviedo-Moderno-CF'):
        continue
    elif (equipo_1 == 'Transportes-Alcaine'):
        continue
    elif (equipo_1 == 'UD-Collerense'):
        continue
    elif (equipo_1 == 'CE-Sant-Gabriel'):
        continue
    elif (equipo_1 == 'Levante-Las-Planas'):
        continue
    elif (equipo_1 == 'Granada'):
        continue






    url = 'https://www.livefutbol.com/equipos/'+equipo_1+'/9/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    eq = soup.find_all('div', class_='data')
    print('primerfor '+url)
    for x in (eq[1].table.find_all('tr')):
        if contador != False:
            tag = x.find_all('td')
            club.append(equipo)
            for y in list(range(0, 4)):
                if y == 0:
                    #               tiempo_activo.append(tag[y].text)
                    fecha_completa = tag[y].text
                    lista_fecha_completa = fecha_completa.split(' - ')
                    fecha_inicio = lista_fecha_completa[0].replace('.', '-')
                    fecha_fin = lista_fecha_completa[1].replace('.', '-')
                    fecha_activo_inicio.append(fecha_inicio)
                    fecha_activo_fin.append(fecha_fin)

                elif y == 1:
                    entrenador.append(tag[y].text)
                elif y == 2:
                    pais.append(tag[y].img.get('title'))
                else:
                    #                fecha_nacimiento.append(tag[y].text)
                    fecha_nacimiento_ = tag[y].text
                    fecha_nacimiento_ = fecha_nacimiento_.replace('.', '-')
                    fecha_nacimiento.append(fecha_nacimiento_)

        else:
            contador = True

df = pd.DataFrame({'club':club,'fecha_activo_inicio':fecha_activo_inicio,'fecha_activo_fin':fecha_activo_fin,'entrenador':entrenador,'pais':pais,'fecha_nacimiento':fecha_nacimiento})

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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_laliga_femenina',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)