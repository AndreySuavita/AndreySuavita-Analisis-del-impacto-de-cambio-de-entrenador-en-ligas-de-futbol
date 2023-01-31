from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['PSV Eindhoven', 'FC Twente', 'SBV Excelsior', 'ADO Den Haag',
       'Feyenoord', 'vv Alkmaar', 'PEC Zwolle', 'AFC Ajax',
       'sc Heerenveen', 'Excelsior Barendrecht', "Achilles'29",
       'SC Telstar VVNH', 'FC Utrecht', 'FC Zwolle', 'VVV-Venlo',
       'AZ Alkmaar', 'Willem II', 'Roda JC Kerkrade']
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
    elif (equipo_1 == 'PSV-Eindhoven'):
        equipo_1 = 'psv-eindhoven-frauen'
    elif (equipo_1 == 'FC-Twente'):
        equipo_1 = 'fc-twente-frauen'
    elif (equipo_1 == 'SBV-Excelsior'):
        equipo_1 = 'sbv-excelsior-frauen'
    elif (equipo_1 == 'ADO-Den-Haag'):
        equipo_1 = 'ado-den-haag-frauen'
    elif (equipo_1 == 'Feyenoord'):
        equipo_1 = 'feyenoord-frauen'
    elif (equipo_1 == 'vv-Alkmaar'):
        equipo_1 = 'vv-alkmaar-frauen'
    elif (equipo_1 == 'PEC-Zwolle'):
        equipo_1 = 'pec-zwolle-frauen'
    elif (equipo_1 == 'AFC-Ajax'):
        equipo_1 = 'afc-ajax-frauen'
    elif (equipo_1 == 'sc-Heerenveen'):
        equipo_1 = 'sc-heerenveen-frauen'
    elif (equipo_1 == 'Excelsior-Barendrecht'):
        equipo_1 = 'sbv-excelsior-frauen'
    elif (equipo_1 == "Achilles'29"):
        equipo_1 = 'achilles29-frauen'
    elif (equipo_1 == "SC-Telstar-VVNH"):
        equipo_1 = 'vv-alkmaar-frauen'
    elif (equipo_1 == "FC-Utrecht"):
        equipo_1 = 'fc-utrecht-frauen'
    elif (equipo_1 == "FC-Zwolle"):
        equipo_1 = 'pec-zwolle-frauen'
    elif (equipo_1 == "VVV-Venlo"):
        equipo_1 = 'vvv-venlo-frauen'
    elif (equipo_1 == "AZ-Alkmaar"):
        equipo_1 = 'az-alkmaar-frauen'
    elif (equipo_1 == "Willem-II"):
        equipo_1 = 'willem-ii-frauen'
    elif (equipo_1 == "Roda-JC-Kerkrade"):
        equipo_1 = 'roda-jc-kerkrade-frauen'




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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_eredivisie_femenina',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)