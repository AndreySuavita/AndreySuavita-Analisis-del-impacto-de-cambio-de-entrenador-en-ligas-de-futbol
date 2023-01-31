from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['SK Brann', 'Stabæk FK', 'Rosenborg BK', 'Vålerenga IF',
       'Avaldsnes IL', 'Kolbotn IL', 'Lyn Oslo', 'Arna-Bjørnar',
       'Lillestrøm SK', 'Røa IL', 'Klepp IL', 'IL Sandviken', 'FL Fart',
       'SK Trondheims-Ørn', 'IK Grand', 'Medkila IL', 'Urædd FK',
       'Amazon Grimstad', 'Kattem IL', 'Linderud-Grei', 'IF Fløya',
       'FK Donn', 'Fortuna Ålesund', 'Team Strømmen']
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
    elif (equipo_1 == 'Stabæk-FK'):
        equipo_1 = 'stabaek-fk'
    elif (equipo_1 == 'Vålerenga-IF'):
        equipo_1 = 'valerenga-if'
    elif (equipo_1 == 'Lillestrøm-SK'):
        equipo_1 = 'lillestroem-sk'
    elif (equipo_1 == 'Røa-IL'):
        equipo_1 = 'roea-il'
    elif (equipo_1 == 'SK-Trondheims-Ørn'):
        equipo_1 = 'rosenborg-bk'
    elif (equipo_1 == 'IK-Graasnd'):
        equipo_1 = 'ik-grand'
    elif (equipo_1 == 'Amazon-Griasdmstad'):
        equipo_1 = 'amazon-grimstad'
    elif (equipo_1 == 'Team-Strømmen'):
        equipo_1 = 'lillestroem-sk'

 

    elif (equipo_1 in ['Lyn-Oslo','Arna-Bjørnar','Klepp-IL','FL-Fart','IK-Grand','Medkila-IL','Urædd-FK','Amazon-Grimstad','Kattem-IL',
                         'Linderud-Grei','IF-Fløya','FK-Donn','Fortuna-Ålesund']):
        continue




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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_toppserien_noruega_femenina',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)