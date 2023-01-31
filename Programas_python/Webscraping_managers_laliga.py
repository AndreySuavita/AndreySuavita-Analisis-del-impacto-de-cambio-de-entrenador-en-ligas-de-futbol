from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Valencia', 'Cádiz CF', 'Mallorca', 'Osasuna', 'Alavés', 'Celta',
       'Barcelona', 'Sevilla', 'Villarreal', 'Elche', 'Betis', 'Espanyol',
       'Granada', 'Athletic', 'Real Sociedad', 'Atlético', 'Levante',
       'Getafe', 'Rayo', 'Real Madrid', 'Eibar', 'Valladolid', 'Huesca',
       'Leganés', 'Girona', 'Deportivo', 'Málaga', 'Las Palmas',
       'Sporting', 'Almería', 'Córdoba', 'Zaragoza', 'Real Racing',
       'Hércules CF', 'Tenerife', 'Xerez CD', 'Numancia', 'RC Recreativo',
       'Real Murcia', 'Gimnàstic', 'Albacete', 'Real Oviedo',
       'CF Extremadura', 'UD Salamanca', 'SD Compostela', 'CP Mérida',
       'CD Logroñés', 'UE Lleida', 'Real Burgos', 'CD Castellón',
       'CE Sabadell', 'AD Almería', 'Burgos CF', 'Pontevedra CF',
       'Real Jaén', 'CD Condal', 'CyD Leonesa', 'Atlético Tetuán',
       'CD Alcoyano', 'Donostia FC', 'Arenas de Getxo', 'Real Unión',
       'CE Europa']
equipos_fc=['Valencia','Villarreal','Elche','Granada','Getafe']
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
        equipo_1 = equipo_1+"-cf"
    elif (equipo_1 == 'Cádiz-CF'):
        equipo_1 = 'cadiz-cf'
    elif (equipo_1 == 'Mallorca'):
        equipo_1 = 'rcd-mallorca'
    elif (equipo_1 == 'Osasuna'):
        equipo_1 = 'ca-osasuna'
    elif (equipo_1 == 'Alavés'):
        equipo_1 = 'cd-alaves'
    elif (equipo_1 == 'Celta'):
        equipo_1 = 'celta-vigo'
    elif (equipo_1 == 'Barcelona'):
        equipo_1 = 'fc-barcelona'
    elif (equipo_1 == 'Sevilla'):
        equipo_1 = 'sevilla-fc'
    elif (equipo_1 == 'Betis'):
        equipo_1 = 'real-betis'
    elif (equipo_1 == 'Espanyol'):
        equipo_1 = 'espanyol-barcelona'
    elif (equipo_1 == 'Athletic'):
        equipo_1 = 'athletic-bilbao'
    elif (equipo_1 == 'Atlético'):
        equipo_1 = 'atletico-madrid'
    elif (equipo_1 == 'Levante'):
        equipo_1 = 'levante-ud'
    elif (equipo_1 == 'Rayo'):
        equipo_1 = 'rayo-vallecano'
    elif (equipo_1 == 'Eibar'):
        equipo_1 = 'sd-eibar'
    elif (equipo_1 == 'Valladolid'):
        equipo_1 = 'real-valladolid'
    elif (equipo_1 == 'Huesca'):
        equipo_1 = 'sd-huesca'
    elif (equipo_1 == 'Leganés'):
        equipo_1 = 'cd-leganes'
    elif (equipo_1 == 'Girona'):
        equipo_1 = 'girona-fc'
    elif (equipo_1 == 'Deportivo'):
        equipo_1 = 'deportivo-la-coruna'
    elif (equipo_1 == 'Málaga'):
        equipo_1 = 'malaga-cf'
    elif (equipo_1 == 'Las-Palmas'):
        equipo_1 = 'ud-las-palmas'
    elif (equipo_1 == 'Sporting'):
        equipo_1 = 'sporting-gijon'
    elif (equipo_1 == 'Almería'):
        equipo_1 = 'ud-almeria'
    elif (equipo_1 == 'Córdoba'):
        equipo_1 = 'cordoba-cf'
    elif (equipo_1 == 'Zaragoza'):
        equipo_1 = 'real-zaragoza'
    elif (equipo_1 == 'Real-Racing'):
        equipo_1 = 'racing-santander'
    elif (equipo_1 == 'Hércules-CF'):
        equipo_1 = 'hercules-cf'
    elif (equipo_1 == 'Tenerife'):
        equipo_1 = 'cd-tenerife'
    elif (equipo_1 == 'Numancia'):
        equipo_1 = 'cd-numancia'
    elif (equipo_1 == 'RC-Recreativo'):
        equipo_1 = 'recreativo-huelva'
    elif (equipo_1 == 'Gimnàstic'):
        equipo_1 = 'gimnastic'
    elif (equipo_1 == 'CP-Mérida'):
        equipo_1 = 'merida-ad'
    elif (equipo_1 == 'CD-Logroñés'):
        equipo_1 = 'cd-logrones'
    elif (equipo_1 == 'UE-Lleida'):
        equipo_1 = 'lleida-esportiu'
    elif (equipo_1 == 'Real-Burgos'):
        equipo_1 = 'burgos-cf'
    elif (equipo_1 == 'CD-Castellón'):
        equipo_1 = 'cd-castellon'
    elif (equipo_1 == 'AD-Almería'):
        equipo_1 = 'ad-almeria'
    elif (equipo_1 == 'Real-Jaén'):
        equipo_1 = 'real-jaen'
    elif (equipo_1 == 'CyD-Leonesa'):
        equipo_1 = 'cd-leonesa'
    elif (equipo_1 == 'Atlético-Tetuán'):
        equipo_1 = 'atletico-tetuan'
    elif (equipo_1 == 'Donostia-FC'):
        equipo_1 = 'real-sociedad'
    elif (equipo_1 == 'Real-Unión'):
        equipo_1 = 'real-union'
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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_laliga',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)