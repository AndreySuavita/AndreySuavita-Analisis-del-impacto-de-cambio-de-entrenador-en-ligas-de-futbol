from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Hoffenheim', 'Wolfsburgo', 'SGS Essen', 'Eintracht Frankfurt',
       'FC Carl Zeiss Jena', 'Bayern Múnich', 'Turbine Potsdam',
       'SC Sand', 'Werder Bremen', 'SC Freiburg', 'Bayer Leverkusen',
       'Colonia', 'MSV Duisburg', 'SV Meppen', '1. FFC Frankfurt',
       'FF USV Jena', 'Bor. Mönchengladbach', 'Herforder SV',
       'VfL Sindelfingen', 'BV Cloppenburg', 'FCR 2001 Duisburg',
       'SC 07 Bad Neuenahr', 'FSV Gütersloh 2009', 'Hamburgo',
       '1. FC Lok Leipzig', 'SG Essen-Schönebeck', '1. FC Saarbrücken',
       'TeBe Berlin', 'TSV Crailsheim', 'SG Wattenscheid 09',
       'Heike Rheine', 'Brauweiler Pulheim', 'FSV Frankfurt',
       'TuS Niederkirchen', 'WSV Wolfsburg-Wendschott', 'FCR Duisburg 55',
       'FFC Flaesheim-Hillen', 'Sportfreunde Siegen', '1. FC Nürnberg',
       'Grün-Weiß Brauweiler', 'SSV Turbine Potsdam', 'SG Praunheim',
       'Eintracht Rheine', 'SC Klinge-Seckach']
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
    elif (equipo_1 == 'Hoffenheim'):
        equipo_1 = '1899-hoffenheim-frauen'
    elif (equipo_1 == 'Wolfsburgo'):
        equipo_1 = 'vfl-wolfsburg-frauen'
    elif (equipo_1 == 'SGS-Essen'):
        equipo_1 = 'sgs-essen-frauen'
    elif (equipo_1 == 'Eintracht-Frankfurt'):
        equipo_1 = 'eintracht-frankfurt-frauen'
    elif (equipo_1 == 'FC-Carl-Zeiss-Jena'):
        equipo_1 = 'fc-carl-zeiss-jena-frauen'
    elif (equipo_1 == 'Bayern-Múnich'):
        equipo_1 = 'bayern-muenchen-frauen'
    elif (equipo_1 == 'Turbine-Potsdam'):
        equipo_1 = 'turbine-potsdam-frauen'
    elif (equipo_1 == 'SC-Sand'):
        equipo_1 = 'sc-sand-frauen'
    elif (equipo_1 == 'Werder-Bremen'):
        equipo_1 = 'werder-bremen-frauen'
    elif (equipo_1 == 'SC-Freiburg'):
        equipo_1 = 'sc-freiburg-frauen'
    elif (equipo_1 == 'Bayer-Leverkusen'):
        equipo_1 = 'bayer-leverkusen-frauen'
    elif (equipo_1 == 'Colonia'):
        equipo_1 = '1-fc-koeln-frauen'
    elif (equipo_1 == '1.-FFC-Frankfurt'):
        equipo_1 = 'eintracht-frankfurt-frauen'
    elif (equipo_1 == 'MSV-Duisburg'):
        equipo_1 = 'msv-duisburg-frauen'
    elif (equipo_1 == 'SV-Meppen'):
        equipo_1 = 'sv-meppen-frauen'
    elif (equipo_1 == 'FF-USV-Jena'):
        equipo_1 = 'fc-carl-zeiss-jena-frauen'
    elif (equipo_1 == 'Bor.-Mönchengladbach'):
        equipo_1 = 'bor-moenchengladbach-frauen'
    elif (equipo_1 == 'Herforder-SV'):
        equipo_1 = 'herforder-sv-frauen'
    elif (equipo_1 == 'VfL-Sindelfingen'):
        equipo_1 = 'vfl-sindelfingen-frauen'
    elif (equipo_1 == 'BV-Cloppenburg'):
        equipo_1 = 'bv-cloppenburg-frauen'
    elif (equipo_1 == 'FCR-2001-Duisburg'):
        equipo_1 = 'msv-duisburg-frauen'
    elif (equipo_1 == 'SC-07-Bad-Neuenahr'):
        equipo_1 = 'sc-13-bad-neuenahr-frauen'
    elif (equipo_1 == 'FSV-Gütersloh-2009'):
        equipo_1 = 'fsv-guetersloh-2009-frauen'
    elif (equipo_1 == 'Hamburgo'):
        equipo_1 = 'hamburger-sv-frauen'
    elif (equipo_1 == '1.-FC-Lok-Leipzig'):
        equipo_1 = '1-fc-lok-leipzig-frauen'
    elif (equipo_1 == 'SG-Essen-Schönebeck'):
        equipo_1 = 'sgs-essen-frauen'
    elif (equipo_1 == 'Heike-Rheine'):
        equipo_1 = 'heike-rheine-frauen'
    elif (equipo_1 == '1.-FC-Saarbrücken'):
        equipo_1 = '1-fc-saarbruecken-frauen'
    elif (equipo_1 == '1.-FC-Saarbrücken'):
        equipo_1 = '1-fc-saarbruecken-frauen'
    elif (equipo_1 == 'TeBe-Berlin'):
        equipo_1 = 'tebe-berlin-frauen'
    elif (equipo_1 == 'TSV-Crailsheim'):
        equipo_1 = 'tsv-crailsheim-frauen'
    elif (equipo_1 == 'SG-Wattenscheid-09'):
        equipo_1 = 'sg-wattenscheid-09-frauen'
    elif (equipo_1 == 'Brauweiler-Pulheim'):
        equipo_1 = 'brauweiler-pulheim-frauen'
    elif (equipo_1 == 'FSV-Frankfurt'):
        equipo_1 = 'fsv-frankfurt-frauen'
    elif (equipo_1 == 'TuS-Niederkirchen'):
        equipo_1 = '1-ffc-08-niederkirchen-frauen'
    elif (equipo_1 == 'WSV-Wolfsburg-Wendschott'):
        equipo_1 = 'wsv-wolfsburg-wendschott-frauen'
    elif (equipo_1 == 'FCR-Duisburg-55'):
        equipo_1 = 'msv-duisburg-frauen'
    elif (equipo_1 == 'FFC-Flaesheim-Hillen'):
        equipo_1 = 'ffc-flaesheim-hillen-frauen'
    elif (equipo_1 == 'Sportfreunde-Siegen'):
        equipo_1 = 'sportfreunde-siegen-frauen'
    elif (equipo_1 == '1.-FC-Nürnberg'):
        equipo_1 = '1-fc-nuernberg-frauen'
    elif (equipo_1 == 'Grün-Weiß-Brauweiler'):
        equipo_1 = 'brauweiler-pulheim-frauen'
    elif (equipo_1 == 'SSV-Turbine-Potsdam'):
        equipo_1 = 'turbine-potsdam-frauen'
    elif (equipo_1 == 'SG-Praunheim'):
        equipo_1 = 'sg-praunheim-frauen'
    elif (equipo_1 == 'Eintracht-Rheine'):
        continue
    elif (equipo_1 == 'SC-Klinge-Seckach'):
        equipo_1 = 'sc-klinge-seckach-frauen'



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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_bundesliga_femenina',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)