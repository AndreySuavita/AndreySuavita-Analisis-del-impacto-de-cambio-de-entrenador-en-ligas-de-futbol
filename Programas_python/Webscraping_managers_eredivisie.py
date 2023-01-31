from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Go Ahead Eagles', 'RKC Waalwijk', 'Heracles Almelo',
       'Fortuna Sittard', 'AFC Ajax', 'SC Cambuur', 'FC Utrecht',
       'PEC Zwolle', 'Willem II', 'NEC Nijmegen', 'sc Heerenveen', 'PSV',
       'Sparta Rotterdam', 'FC Groningen', 'FC Twente', 'Feyenoord',
       'Vitesse', 'AZ Alkmaar', 'FC Emmen', 'VVV-Venlo', 'ADO Den Haag',
       'SBV Excelsior', 'De Graafschap', 'NAC Breda', 'Roda JC Kerkrade',
       'FC Dordrecht', 'FC Volendam', 'RBC Roosendaal', 'FC Den Bosch',
       'FC Zwolle', 'MVV', "Dordrecht '90", "SVV/Dordrecht '90",
       'FC Den Haag', 'SVV Schiedam', 'BVV Den Bosch', 'SBV Haarlem',
       'BV Veendam', "PEC Zwolle '82", "Drechtsteden '79",
       "FC Den Bosch '67", "AZ '67 Alkmaar", "SC Heracles '74",
       'Helmond Sport', 'FC Wageningen', 'HFC Haarlem', 'FC Amsterdam',
       'Telstar', 'SC Eindhoven', 'FC Den Haag-ADO', 'WVV Wageningen',
       'Feijenoord', 'DWS Amsterdam', 'Holland Sport', 'GVAV Groningen',
       'DOS Utrecht', 'FSC Geleen', "Fortuna '54", 'Xerxes/D.H.C.',
       'Sittardia', 'FC Xerxes', 'USV Elinkwijk', 'Groninger VAV',
       'Sportclub Enschede', 'Blauw Wit', 'De Volewijckers',
       'Rapid JC Heerlen', "VV Alkmaar '54", 'NOAD Tilburg', 'SHS',
       'BVC Amsterdam', 'BVV']
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
    elif (equipo_1 == 'PSV'):
        equipo_1 = 'psv-eindhoven'
    elif (equipo_1 == 'FC-Zwolle'):
        equipo_1 = 'pec-zwolle'
    elif (equipo_1 == 'MVV'):
        equipo_1 = 'mvv_2'
    elif (equipo_1 == "Dordrecht-'90" or equipo_1 == "SVV/Dordrecht-'90"):
        equipo_1 = 'fc-dordrecht'
    elif (equipo_1 == "FC-Den-Haag"):
        equipo_1 = 'ado-den-haag'
    elif (equipo_1 == "BVV-Den-Bosch"):
        equipo_1 = 'fc-den-bosch'
    elif (equipo_1 == "SBV-Haarlem"):
        equipo_1 = 'hfc-haarlem'
    elif (equipo_1 == "BV-Veendam"):
        equipo_1 = 'sc-veendam'
    elif (equipo_1 == "PEC-Zwolle-'82"):
        equipo_1 = 'pec-zwolle'
    elif (equipo_1 == "Drechtsteden-'79"):
        equipo_1 = 'fc-dordrecht'
    elif (equipo_1 == "FC-Den-Bosch-'67"):
        equipo_1 = 'fc-den-bosch'
    elif (equipo_1 == "AZ-'67-Alkmaar"):
        equipo_1 = 'az-alkmaar'
    elif (equipo_1 == "SC-Heracles-'74"):
        equipo_1 = 'heracles-almelo'
    elif (equipo_1 == "SC-Eindhoven"):
        equipo_1 = 'fc-eindhoven'
    elif (equipo_1 == "FC-Den-Haag-ADO"):
        equipo_1 = 'ado-den-haag'
    elif (equipo_1 == "WVV-Wageningen"):
        equipo_1 = 'fc-wageningen'
    elif (equipo_1 == "Feijenoord"):
        equipo_1 = 'feyenoord'
    elif (equipo_1 == "DWS-Amsterdam"):
        equipo_1 = 'afc-dws'
    elif (equipo_1 == "GVAV-Groningen"):
        equipo_1 = 'fc-groningen'
    elif (equipo_1 == "DOS-Utrecht"):
        equipo_1 = 'fc-utrecht'
    elif (equipo_1 == "DOS-Utrecht"):
        equipo_1 = 'fc-utrecht'
    elif (equipo_1 == "FSC-Geleen"):
        equipo_1 = 'fortuna-sittard'
    elif (equipo_1 == "Fortuna-'54"):
        equipo_1 = 'fortuna-54'
    elif (equipo_1 == "Xerxes/D.H.C."):
        equipo_1 = 'xerxes-dzb'
    elif (equipo_1 == "FC-Xerxes"):
        equipo_1 = 'xerxes-dzb'
    elif (equipo_1 == "Groninger-VAV"):
        equipo_1 = 'fc-groningen'
    elif (equipo_1 == "Sportclub-Enschede"):
        equipo_1 = 'fc-twente'
    elif (equipo_1 == "Rapid-JC-Heerlen"):
        equipo_1 = 'roda-jc-kerkrade'
    elif (equipo_1 == "VV-Alkmaar-'54"):
        equipo_1 = 'az-alkmaar'
    elif (equipo_1 == "SHS"):
        equipo_1 = 'holland-sport'
    elif (equipo_1 == "BVC-Amsterdam"):
        continue
    elif (equipo_1 == "BVV"):
        equipo_1 = 'fc-den-bosch'

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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_eredivisie',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)