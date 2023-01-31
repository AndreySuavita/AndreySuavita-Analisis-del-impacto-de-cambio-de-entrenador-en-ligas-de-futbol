from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['AIK Solna', 'Djurgårdens IF', 'Eskilstuna United',
       'IF Brommapojkarna', 'Kristianstads DFF', 'KIF Örebro DFF',
       'Vittsjö GIK', 'Linköpings FC', 'Umeå IK FF', 'Hammarby IF',
       'Piteå IF', 'IFK Kalmar', 'BK Häcken', 'FC Rosengård', 'Växjö DFF',
       'Kopparbergs/Göteborg FC', 'IK Uppsala', 'IF Limhamn Bunkeflo',
       'Kungsbacka DFF', 'Kvarnsvedens IK', 'Mallbackens IF', 'Tyresö FF',
       'Jitex BK', 'Sunnanå SK', 'LdB FC Malmö', 'Dalsjöfors GoIF',
       'Stattena IF']
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
    elif (equipo_1 == 'Djurgårdens-IF'):
        equipo_1 = 'djurgardens-if'
    elif (equipo_1 == 'KIF-Örebro-DFF'):
        equipo_1 = 'kif-oerebro'
    elif (equipo_1 == 'Vittsjö-GIK'):
        equipo_1 = 'vittsjoe-gik'
    elif (equipo_1 == 'Linköpings-FC'):
        equipo_1 = 'linkoepings-fc'
    elif (equipo_1 == 'Umeå-IK-FF'):
        equipo_1 = 'umea-ik'
    elif (equipo_1 == 'Piteå-IF'):
        equipo_1 = 'pitea-if'
    elif (equipo_1 == 'BK-Häcken'):
        equipo_1 = 'bk-haecken'
    elif (equipo_1 == 'FC-Rosengård'):
        equipo_1 = 'fc-rosengard'
    elif (equipo_1 == 'Växjö-DFF'):
        equipo_1 = 'vaexjoe-dff'
    elif (equipo_1 == 'Kopparbergs/Göteborg-FC'):
        equipo_1 = 'bk-haecken'
    elif (equipo_1 == 'Tyresö-FF'):
        equipo_1 = 'tyresoe-ff'
    elif (equipo_1 == 'LdB-FC-Malmö'):
        equipo_1 = 'fc-rosengard'
    elif (equipo_1 in ['Eintracht-Rheine','IF-Limhamn-Bunkeflo','Kungsbacka-DFF','Kvarnsvedens-IK','Sunnanå-SK','Dalsjöfors-GoIF']):
        continue
    elif (equipo_1 == 'SC-Klinge-Seckach'):
        equipo_1 = 'sc-klinge-seckach-frauen'



    url = 'https://www.livefutbol.com/equipos/'+equipo_1+'-frauen/9/'
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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_damallsvenskan_suecia_femenina',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)