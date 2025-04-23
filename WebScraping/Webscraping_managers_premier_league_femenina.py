from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Manchester United WFC', 'Aston Villa', 'Everton',
       'Tottenham Hotspur WFC', 'Arsenal', 'Brighton & Hove Albion WFC',
       'West Ham United WFC', 'Chelsea', 'Birmingham City WFC',
       'Reading WFC', 'Leicester City WFC', 'Manchester City WFC',
       'Bristol City WFC', 'Liverpool', 'Yeovil Town LFC']
equipos_fc=[]
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
    elif (equipo_1 == 'Manchester-United-WFC'):
        equipo_1 = 'manchester-united-wfc-frauen'
    elif (equipo_1 == 'Aston-Villa'):
        equipo_1 = 'aston-villa-wfc-frauen'
    elif (equipo_1 == 'Everton'):
        equipo_1 = 'everton-fc-frauen'
    elif (equipo_1 == 'Tottenham-Hotspur-WFC'):
        equipo_1 = 'tottenham-hotspur-wfc-frauen'
    elif (equipo_1 == 'Arsenal'):
        equipo_1 = 'arsenal-wfc-frauen'
    elif (equipo_1 == 'Brighton-&-Hove-Albion-WFC'):
        equipo_1 = 'brighton-hove-albion-wfc-frauen'
    elif (equipo_1 == 'West-Ham-United-WFC'):
        equipo_1 = 'west-ham-united-wfc-frauen'
    elif (equipo_1 == 'Chelsea'):
        equipo_1 = 'chelsea-fc-women-frauen'
    elif (equipo_1 == 'Birmingham-City-WFC'):
        equipo_1 = 'birmingham-city-wfc-frauen'
    elif (equipo_1 == 'Reading-WFC'):
        equipo_1 = 'reading-wfc-frauen'
    elif (equipo_1 == 'Leicester-City-WFC'):
        equipo_1 = 'leicester-city-wfc-frauen'
    elif (equipo_1 == 'Manchester-City-WFC'):
        equipo_1 = 'manchester-city-wfc-frauen'
    elif (equipo_1 == 'Bristol-City-WFC'):
        equipo_1 = 'bristol-city-wfc-frauen'
    elif (equipo_1 == 'Liverpool'):
        equipo_1 = 'liverpool-fc-women-frauen'
    elif (equipo_1 == 'Yeovil-Town-LFC'):
        equipo_1 = 'yeovil-town-lfc-frauen'


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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_premier_league_femenina',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)