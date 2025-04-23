from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Mónaco', 'Lyon', 'Troyes', 'Rennes', 'Saint-Étienne',
       'Girondins de Burdeos', 'Niza', 'RC Strasbourg', 'FC Metz',
       'Montpellier', 'Lorient', 'Lille', 'París Saint-Germain', 'Angers',
       'Clermont Foot', 'Nantes', 'Stade Brest', 'Stade de Reims',
       'RC Lens', 'Marsella', 'Dijon FCO', 'Nîmes Olympique', 'Toulouse',
       'Amiens SC', 'Guingamp', 'Caen', 'Bastia', 'AS Nancy',
       'Gazélec Ajaccio', 'Évian Thonon Gaillard', 'Valenciennes FC',
       'AC Ajaccio', 'FC Sochaux', 'AJ Auxerre', 'AC Arles-Avignon',
       'Grenoble Foot 38', 'Le Mans UC 72', 'US Boulogne', 'Le Havre AC',
       'CS Sedan', 'FC Istres', 'AS Cannes', 'LB Châteauroux',
       'FC Gueugnon', 'FC Martigues', 'US Valenciennes-Anzin',
       'SC Toulon', 'Brest Armorique FC', 'Racing Club de France',
       'FC Mulhouse', 'Stade Laval', 'Matra Racing', 'Chamois Niortais',
       'Tours FC', 'FC Rouen', 'Sporting Club de Toulon', 'Paris FC',
       'Association Sportive Avignonaise', 'Red Star FC', 'AS Angoulême',
       'AS Aixoise', 'Stade de Paris FC', 'UA Sedan-Torcy',
       'Stade Français FC', 'FC Nancy', 'Limoges FC', 'Olympique Alès',
       'AS Béziers', 'RC Roubaix', 'FC Sète', 'Stade Red Star',
       'AS Cannes-Grasse', 'SR Colmar', 'Stade Français',
       'Red Star Olympique Audonien', 'Red Star Olympique', 'FC Antibes',
       'Excelsior Roubaix', 'SC Fives Lille', 'Olympique Lillois Lille',
       'CS Metz', 'SC Nimes', 'CA Paris (old)', 'Club Francais Paris',
       'Hyères FC']
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
        equipo_1 = equipo_1
    elif (equipo_1 == 'Mónaco'):
        equipo_1 = 'as-monaco'
    elif (equipo_1 == 'Lyon'):
        equipo_1 = 'olympique-lyon'
    elif (equipo_1 == 'Troyes'):
        equipo_1 = 'estac-troyes'
    elif (equipo_1 == 'Rennes'):
        equipo_1 = 'stade-rennes'
    elif (equipo_1 == 'Saint-Étienne'):
        equipo_1 = 'as-saint-etienne'
    elif (equipo_1 == 'Girondins-de-Burdeos'):
        equipo_1 = 'girondins-bordeaux'
    elif (equipo_1 == 'Niza'):
        equipo_1 = 'ogc-nice'
    elif (equipo_1 == 'Montpellier'):
        equipo_1 = 'montpellier-hsc'
    elif (equipo_1 == 'Lorient'):
        equipo_1 = 'fc-lorient'
    elif (equipo_1 == 'Lille'):
        equipo_1 = 'lille-osc'
    elif (equipo_1 == 'París-Saint-Germain'):
        equipo_1 = 'paris-saint-germain'
    elif (equipo_1 == 'Angers'):
        equipo_1 = 'angers-sco'
    elif (equipo_1 == 'Nantes'):
        equipo_1 = 'fc-nantes'
    elif (equipo_1 == 'Stade-de-Reims'):
        equipo_1 = 'stade-reims'
    elif (equipo_1 == 'Marsella'):
        equipo_1 = 'olympique-marseille'
    elif (equipo_1 == 'Nîmes-Olympique'):
        equipo_1 = 'nimes-olympique'
    elif (equipo_1 == 'Toulouse'):
        equipo_1 = 'toulouse-fc'
    elif (equipo_1 == 'Guingamp'):
        equipo_1 = 'ea-guingamp'
    elif (equipo_1 == 'Caen'):
        equipo_1 = 'sm-caen'
    elif (equipo_1 == 'Bastia'):
        equipo_1 = 'sc-bastia'
    elif (equipo_1 == 'Gazélec-Ajaccio'):
        equipo_1 = 'gfc-ajaccio'
    elif (equipo_1 == 'Évian-Thonon-Gaillard'):
        equipo_1 = 'thonon-evian-fc'
    elif (equipo_1 == 'Le-Mans-UC-72'):
        equipo_1 = 'le-mans-fc'
    elif (equipo_1 == 'LB-Châteauroux'):
        equipo_1 = 'lb-chateauroux'
    elif (equipo_1 == 'US-Valenciennes-Anzin'):
        equipo_1 = 'valenciennes-fc'
    elif (equipo_1 == 'Brest-Armorique-FC'):
        equipo_1 = 'stade-brest'
    elif (equipo_1 == 'Brest-Armorique-FC'):
        equipo_1 = 'stade-brest'
    elif (equipo_1 == 'Matra-Racing'):
        equipo_1 = 'racing-club-de-france'
    elif (equipo_1 == 'Association-Sportive-Avignonaise'):
        equipo_1 = 'avenir-club-avignonnais'
    elif (equipo_1 == 'Red-Star-FC'):
        equipo_1 = 'red-star-fc_2'
    elif (equipo_1 == 'AS-Angoulême'):
        equipo_1 = 'angouleme-cfc'
    elif (equipo_1 == 'Stade-de-Paris-FC'):
        equipo_1 = 'stade-francais'
    elif (equipo_1 == 'UA-Sedan-Torcy'):
        equipo_1 = 'cs-sedan'
    elif (equipo_1 == 'Stade-Français-FC'):
        equipo_1 = 'stade-francais'
    elif (equipo_1 == 'Olympique-Alès'):
        equipo_1 = 'olympique-ales'
    elif (equipo_1 == 'AS-Béziers'):
        equipo_1 = 'as-beziers'
    elif (equipo_1 == 'FC-Sète'):
        equipo_1 = 'fc-sete'
    elif (equipo_1 == 'Stade-Red-Star'):
        equipo_1 = 'stade-francais'
    elif (equipo_1 == 'AS-Cannes-Grasse'):
        equipo_1 = 'as-cannes'
    elif (equipo_1 == 'Stade-Français'):
        equipo_1 = 'stade-francais'
    elif (equipo_1 == 'Red-Star-Olympique-Audonien' or equipo_1 == 'Red-Star-Olympique'):
        equipo_1 = 'red-star-fc_2'
    elif (equipo_1 == 'Red-Star-Olympique'):
        equipo_1 = 'red-star-fc_2'
    elif (equipo_1 == 'CS-Metz'):
        equipo_1 = 'fc-metz'
    elif (equipo_1 == 'CA-Paris-(old)'):
        equipo_1 = 'ca-paris-old'
    elif (equipo_1 == 'SC-Nimes'):
        equipo_1 = 'nimes-olympique'
    elif (equipo_1 == 'Hyères-FC'):
        equipo_1 = 'hyeres-fc'
    elif (equipo_1 == 'Excelsior-Roubaix' or equipo_1 == 'SC-Fives-Lille' or equipo_1 == 'Club-Francais-Paris'):
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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_ligue_1',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)