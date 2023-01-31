from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Lyon', 'Saint-Étienne', 'Dijon FCO', 'Paris FC', 'ASJ Soyaux',
       'París Saint-Germain', 'FC Fleury 91', 'Montpellier',
       'Girondins Bordeaux', 'GPSO 92 Issy', 'Stade Reims', 'Guingamp',
       'Le Havre AC', 'Olympique Marseille', 'FC Metz-Algrange',
       'Lille OSC', 'Rodez Aveyron', 'ASPTT Albi', 'Juvisy FCF',
       'VGA Saint-Maur', 'La Roche ESOF', 'Nîmes Métropole Gard',
       'Issy FF', 'Arras FCF', 'Henin-Beaumont', 'Nord Allier Yzeure',
       'AS Muretaine', 'FC Vendenheim', 'Toulouse', 'Le Mans FC']
equipos_fc=['Le-Mans-FC']
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
    elif (equipo_1 == 'Lyon'):
        equipo_1 = 'olympique-lyon-frauen'
    elif (equipo_1 == 'Saint-Étienne'):
        equipo_1 = 'as-saint-etienne-frauen'
    elif (equipo_1 == 'Dijon-FCO'):
        equipo_1 = 'dijon-fco-frauen'
    elif (equipo_1 == 'Paris-FC'):
        equipo_1 = 'paris-fc-frauen'
    elif (equipo_1 == 'ASJ-Soyaux'):
        equipo_1 = 'asj-soyaux-frauen'
    elif (equipo_1 == 'París-Saint-Germain'):
        equipo_1 = 'paris-saint-germain-frauen'
    elif (equipo_1 == 'FC-Fleury-91'):
        equipo_1 = 'fc-fleury-91-frauen'
    elif (equipo_1 == 'Montpellier'):
        equipo_1 = 'montpellier-hsc-frauen'
    elif (equipo_1 == 'Girondins-Bordeaux'):
        equipo_1 = 'girondins-bordeaux-frauen'
    elif (equipo_1 == 'GPSO-92-Issy'):
        equipo_1 = 'gpso-92-issy-frauen'
    elif (equipo_1 == 'Stade-Reims'):
        equipo_1 = 'stade-reims-frauen'
    elif (equipo_1 == 'Guingamp'):
        equipo_1 = 'ea-guingamp-frauen'
    elif (equipo_1 == 'Le-Havre-AC'):
        equipo_1 = 'le-havre-ac-frauen'
    elif (equipo_1 == 'Olympique-Marseille'):
        equipo_1 = 'olympique-marseille-frauen'
    elif (equipo_1 == 'FC-Metz-Algrange'):
        equipo_1 = 'fc-metz-algrange-frauen'
    elif (equipo_1 == 'Lille-OSC'):
        equipo_1 = 'lille-osc-frauen'
    elif (equipo_1 == 'Rodez-Aveyron'):
        equipo_1 = 'rodez-aveyron-frauen'
    elif (equipo_1 == 'ASPTT-Albi'):
        equipo_1 = 'asptt-albi-frauen'
    elif (equipo_1 == 'Juvisy-FCF'):
        equipo_1 = 'paris-fc-frauen'
    elif (equipo_1 == 'VGA-Saint-Maur'):
        equipo_1 = 'vga-saint-maur-frauen'
    elif (equipo_1 == 'La-Roche-ESOF'):
        continue
    elif (equipo_1 == 'Nîmes-Métropole-Gard'):
        continue
    elif (equipo_1 == 'Arras-FCF'):
        continue
    elif (equipo_1 == 'Henin-Beaumont'):
        continue
    elif (equipo_1 == 'Nord-Allier-Yzeure'):
        continue
    elif (equipo_1 == 'AS-Muretaine'):
        continue
    elif (equipo_1 == 'FC-Vendenheim'):
        continue
    elif (equipo_1 == 'Toulouse'):
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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_ligue_1_femenina',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)