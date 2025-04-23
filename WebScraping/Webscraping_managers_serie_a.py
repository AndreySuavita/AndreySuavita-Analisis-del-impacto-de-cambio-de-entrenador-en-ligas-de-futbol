from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Hellas Verona', 'Inter', 'Empoli', 'Torino', 'Bolonia', 'Udinese',
       'Nápoles', 'Roma', 'Cagliari Calcio', 'Sampdoria', 'Atalanta',
       'Lazio', 'Fiorentina', 'Juventus', 'Génova', 'Sassuolo', 'Milan',
       'US Salernitana 1919', 'Spezia Calcio', 'Venezia FC',
       'Parma Calcio 1913', 'Benevento Calcio', 'FC Crotone',
       'SPAL 2013 Ferrara', 'US Lecce', 'Brescia Calcio', 'Chievo',
       'Frosinone', 'Palermo', 'Pescara Calcio', 'Carpi', 'AC Cesena',
       'Parma FC', 'AS Livorno', 'Calcio Catania', 'AC Siena',
       'Novara Calcio', 'AS Bari', 'Reggina Calcio', 'FC Messina',
       'Ascoli Calcio', 'Treviso FBC', 'AC Perugia', 'Ancona Calcio',
       'Modena FC', 'Parma AC', 'Piacenza Calcio', 'Calcio Como',
       'AC Venezia', 'Vicenza Calcio', 'Salernitana Sport', 'AC Reggiana',
       'Calcio Padova', 'US Cremonese', 'US Foggia', 'Pisa SC',
       'US Avellino', 'US Catanzaro', 'AC Pistoiese', 'Lanerossi Vicenza',
       'AS Varese 1910', 'Ternana Calcio', 'AC Mantova', 'SPAL Ferrara',
       'Calcio Lecco 1912', 'A.C.R. Messina', 'US Alessandria 1912',
       'US Triestina', 'Aurora Pro Patria', 'Legnano', 'Lucchese',
       'US Livorno', 'Vicenza Virtus', 'US Anconitana', 'Andrea Doria',
       'Sampierdarenese', 'AC Liguria', 'Pro Vercelli', 'Casale']
equipos_fc=['Empoli','Torino','Palermo','Carpi']
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
    elif (equipo_1 == 'Bolonia'):
        equipo_1 = 'bologna-fc'
    elif (equipo_1 == 'Udinese'):
        equipo_1 = 'udinese-calcio'
    elif (equipo_1 == 'Nápoles'):
        equipo_1 = 'ssc-napoli'
    elif (equipo_1 == 'Roma'):
        equipo_1 = 'as-roma'
    elif (equipo_1 == 'Lazio'):
        equipo_1 = 'lazio-roma'
    elif (equipo_1 == 'Fiorentina'):
        equipo_1 = 'acf-fiorentina'
    elif (equipo_1 == 'Génova'):
        equipo_1 = 'genoa-cfc'
    elif (equipo_1 == 'Sassuolo'):
        equipo_1 = 'sassuolo-calcio'
    elif (equipo_1 == 'Milan'):
        equipo_1 = 'ac-milan'
    elif (equipo_1 == 'Chievo'):
        equipo_1 = 'chievo-verona'
    elif (equipo_1 == 'Frosinone'):
        equipo_1 = 'frosinone-calcio'
    elif (equipo_1 == 'AC-Siena'):
        equipo_1 = 'acn-siena-1904'
    elif (equipo_1 == 'AS-Bari'):
        equipo_1 = 'ssc-bari'
    elif (equipo_1 == 'Reggina-Calcio'):
        equipo_1 = 'reggina-1914'
    elif (equipo_1 == 'FC-Messina'):
        equipo_1 = 'acr-messina'
    elif (equipo_1 == 'Treviso-FBC'):
        equipo_1 = 'a-c-d-treviso'
    elif (equipo_1 == 'AC-Perugia'):
        equipo_1 = 'ac-perugia-calcio'
    elif (equipo_1 == 'Ancona-Calcio'):
        equipo_1 = 'ac-ancona'
    elif (equipo_1 == 'Parma-AC'):
        equipo_1 = 'parma-calcio-1913'
    elif (equipo_1 == 'AC-Venezia'):
        equipo_1 = 'venezia-fc'
    elif (equipo_1 == 'Salernitana-Sport'):
        equipo_1 = 'us-salernitana-1919'
    elif (equipo_1 == 'AC-Reggiana'):
        equipo_1 = 'ac-reggiana-1919'
    elif (equipo_1 == 'Pisa-SC'):
        equipo_1 = 'ac-pisa'
    elif (equipo_1 == 'AC-Pistoiese'):
        equipo_1 = 'us-pistoiese'
    elif (equipo_1 == 'Lanerossi-Vicenza'):
        equipo_1 = 'vicenza-virtus'
    elif (equipo_1 == 'SPAL-Ferrara'):
        equipo_1 = 'spal-2013-ferrara'
    elif (equipo_1 == 'A.C.R.-Messina'):
        equipo_1 = 'acr-messina'
    elif (equipo_1 == 'A.C.R.-Messina'):
        equipo_1 = 'acr-messina'
    elif (equipo_1 == 'US-Livorno'):
        equipo_1 = 'as-livorno'



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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_serie_a',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)