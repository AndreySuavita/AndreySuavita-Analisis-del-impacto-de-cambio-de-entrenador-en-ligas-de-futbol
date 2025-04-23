from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Brentford FC', 'Manchester United', 'Burnley FC', 'Chelsea',
       'Everton', 'Leicester City', 'Watford FC', 'Norwich City',
       'Newcastle United', 'Tottenham Hotspur', 'Liverpool',
       'Aston Villa', 'Crystal Palace', 'Leeds United', 'Manchester City',
       'Brighton & Hove Albion', 'Southampton', 'Wolverhampton Wanderers',
       'Arsenal', 'West Ham United', 'Fulham FC', 'West Bromwich Albion',
       'Sheffield United', 'Bournemouth', 'Huddersfield Town',
       'Cardiff City', 'Swansea City', 'Stoke City', 'Hull City',
       'Middlesbrough', 'Sunderland', 'Queens Park Rangers', 'Reading',
       'Wigan Athletic', 'Blackburn Rovers', 'Bolton Wanderers',
       'Birmingham City', 'Blackpool FC', 'Portsmouth FC', 'Derby County',
       'Charlton Athletic', 'Ipswich Town', 'Coventry City',
       'Bradford City', 'Sheffield Wednesday', 'Wimbledon FC',
       'Nottingham Forest', 'Barnsley FC', 'Oldham Athletic',
       'Swindon Town', 'Notts County', 'Luton Town', 'Millwall FC',
       'Oxford United', 'Bristol City', 'Carlisle United',
       'Northampton Town', 'Leyton Orient', 'Preston North End',
       'Grimsby Town', 'Birmingham FC', 'The Wednesday FC', 'Bury FC',
       'Bradford Park Avenue', 'Leicester Fosse',
       'Small Heath Birmingham', 'Glossop North End', 'Darwen',
       'Newton Heath FC', 'Accrington FC']
equipos_fc=['Chelsea','Everton','Liverpool','Southampton','Arsenal','Middlesbrough','Reading',]
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
        equipo_1 = equipo_1+'-fc'
    elif (equipo_1 == 'Brighton-&-Hove-Albion'):
        equipo_1 = 'Brighton-Hove-Albion'
    elif (equipo_1 == 'Bournemouth'):
        equipo_1 = 'afc-bournemouth'
    elif (equipo_1 == 'Sunderland'):
        equipo_1 = 'sunderland-afc'
    elif (equipo_1 == 'Birmingham-FC'):
        equipo_1 = 'birmingham-city'
    elif (equipo_1 == 'The-Wednesday-FC' or equipo_1=='Leicester-Fosse' or equipo_1 =='Small-Heath-Birmingham' or equipo_1== 'Newton-Heath-FC' or equipo_1=='Accrington-FC'):
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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_premier_league',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)