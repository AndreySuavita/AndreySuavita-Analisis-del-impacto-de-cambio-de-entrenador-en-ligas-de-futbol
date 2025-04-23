from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Barracas Central', 'Atlético Tucumán', 'San Lorenzo', 'Banfield',
       'Patronato de Paraná', 'Platense', 'Racing Club',
       'Talleres de Córdoba', 'Unión de Santa Fe', 'Estudiantes',
       'Boca Juniors', 'Defensa y Justicia', 'Rosario Central',
       'Argentinos Juniors', "Newell's Old Boys", 'Gimnasia de La Plata',
       'Aldosivi', 'CA Lanús', 'Huracán', 'Independiente',
       'Arsenal de Sarandí', 'Tigre', 'Sarmiento de Junín', 'River Plate',
       'Colón de Santa Fe', 'Godoy Cruz', 'Vélez Sarsfield',
       'Central Córdoba SdE', 'Belgrano', 'San Martín de San Juan',
       'San Martín de Tucumán', 'Temperley', 'Olimpo de Bahía Blanca',
       'Chacarita Juniors', 'Quilmes', 'Atlético Rafaela',
       'Crucero del Norte', 'Nueva Chicago', 'All Boys',
       'Gimnasia de Jujuy', 'Tiro Federal de Rosario',
       'Instituto de Córdoba', 'Huracán de Tres Arroyos', 'Almagro',
       'Los Andes de Lomas de Zamora', 'Ferro Carril Oeste',
       'Deportivo Español', 'Gimnasia y Tiro de Salta',
       'Huracán de Corrientes', 'Deportivo Mandiyú', 'Chaco For Ever',
       'Racing de Córdoba', 'Armenio', 'Deportivo Italiano']
equipos2=['Barracas Central', 'Atlético Tucumán', 'San Lorenzo', 'Banfield',
       'Patronato de Paraná', 'Platense', 'Racing Club',
       'Talleres de Córdoba', 'Unión de Santa Fe', 'Estudiantes',
       'Boca Juniors', 'Defensa y Justicia', 'Rosario Central',
       'Argentinos Juniors', "Newell's Old Boys", 'Gimnasia de La Plata',
       'Aldosivi', 'CA Lanús', 'Huracán', 'Independiente',
       'Arsenal de Sarandí', 'Tigre', 'Sarmiento de Junín', 'River Plate',
       'Colón de Santa Fe', 'Godoy Cruz', 'Vélez Sarsfield',
       'Central Córdoba SdE', 'Belgrano', 'San Martín de San Juan',
       'San Martín de Tucumán', 'Temperley', 'Olimpo de Bahía Blanca',
       'Chacarita Juniors', 'Quilmes', 'Atlético Rafaela',
       'Crucero del Norte', 'Nueva Chicago', 'All Boys',
       'Gimnasia de Jujuy', 'Tiro Federal de Rosario',
       'Instituto de Córdoba', 'Huracán de Tres Arroyos', 'Almagro',
       'Los Andes de Lomas de Zamora', 'Ferro Carril Oeste',
       'Deportivo Español', 'Gimnasia y Tiro de Salta',
       'Huracán de Corrientes', 'Deportivo Mandiyú', 'Chaco For Ever',
       'Racing de Córdoba', 'Armenio', 'Deportivo Italiano']
#remover tildes y quitar espacios
for y in list(range(len(equipos))):
    x = equipos[y]
    x = x.replace('á','a')
    x = x.replace('é', 'e')
    x = x.replace('í', 'i')
    x = x.replace('ó', 'o')
    x = x.replace('ú', 'u')
    x = x.replace('Á','A')
    x = x.replace('É', 'E')
    x = x.replace('Í', 'I')
    x = x.replace('Ó', 'O')
    x = x.replace('Ú', 'U')
    x = x.replace('ã','a')
    x = x.replace('ê','e')
    x = x.replace(" - ","-")
    equipos[y] = x
equipos_fc=[]
club=[]
fecha_activo_inicio = []
fecha_activo_fin = []
entrenador = []
pais = []
fecha_nacimiento = []
contador=False

for equipo in list(range(len(equipos))):
    contador=False
    equipo_1 = equipos[equipo].replace(' ','-')
    if (equipo_1 in equipos_fc):
        equipo_1 = equipo_1
    elif (equipo_1 == "Newell's-Old-Boys"):
        equipo_1 = 'newells-old-boys'
    elif (equipo_1 == 'Almagro'):
        equipo_1 = 'almagro_3'
    elif (equipo_1 == 'Deportivo-Español'):
        equipo_1 = 'deportivo-espanol_3'
    elif (equipo_1 == 'Stuttgart'):
        equipo_1 = 'vfb-stuttgart'
    elif (equipo_1 == 'Augsburgo'):
        equipo_1 = 'fc-augsburg'
    elif (equipo_1 == 'Mainz'):
        equipo_1 = '1-fsv-mainz-05'
    elif (equipo_1 == 'Colonia'):
        equipo_1 = '1-fc-koeln'
    elif (equipo_1 == 'Hertha'):
        equipo_1 = 'hertha-bsc'
    elif (equipo_1 == 'SpVgg-Greuther-Fürth'):
        equipo_1 = 'spvgg-greuther-fuerth'
    elif (equipo_1 == 'Hoffenheim'):
        equipo_1 = '1899-hoffenheim'
    elif (equipo_1 == 'Bayern-Múnich'):
        equipo_1 = 'bayern-muenchen'
    elif (equipo_1 == 'Schalke'):
        equipo_1 = 'fc-schalke-04'
    elif (equipo_1 == 'Fortuna-Düsseldorf'):
        equipo_1 = 'fortuna-duesseldorf'
    elif (equipo_1 == 'Hannover'):
        equipo_1 = 'hannover-96'
    elif (equipo_1 == '1.-FC-Nürnberg'):
        equipo_1 = '1-fc-nuernberg'
    elif (equipo_1 == 'Hamburgo'):
        equipo_1 = 'hamburger-sv'
    elif (equipo_1 == 'Ingolstadt'):
        equipo_1 = 'fc-ingolstadt-04'
    elif (equipo_1 == 'Darmstadt'):
        equipo_1 = 'sv-darmstadt-98'
    elif (equipo_1 == '1.-FC-Kaiserslautern'):
        equipo_1 = '1-fc-kaiserslautern'
    elif (equipo_1 == 'FC-St.-Pauli'):
        equipo_1 = 'fc-st-pauli'
    elif (equipo_1 == 'TSV-1860-München'):
        equipo_1 = 'tsv-1860-muenchen'
    elif (equipo_1 == 'Bayer-05-Uerdingen'):
        equipo_1 = 'tsv-1860-muenchen'
    elif (equipo_1 == 'VfB-Leipzig'):
        equipo_1 = 'tsv-1860-muenchen'
    elif (equipo_1 == 'VfB-Leipzig'):
        equipo_1 = '1-fc-lok-leipzig'
    elif (equipo_1 == '1.-FC-Saarbrücken'):
        equipo_1 = '1-fc-saarbruecken'
    elif (equipo_1 == 'Blau-Weiß-90-Berlin'):
        equipo_1 = 'blau-weiss-90-berlin'
    elif (equipo_1 == 'Fortuna-Köln'):
        equipo_1 = 'fortuna-koeln'
    elif (equipo_1 == 'Rot-Weiß-Oberhausen'):
        equipo_1 = 'rot-weiss-oberhausen'
    elif (equipo_1 == 'Frankfurter-SG-Eintracht'):
        equipo_1 = 'eintracht-frankfurt'
    elif (equipo_1 == 'Meidericher-SV'):
        equipo_1 = 'msv-duisburg'
    elif (equipo_1 == 'Tasmania-1900-Berlin'):
        equipo_1 = 'sv-tasmania-berlin'
    elif (equipo_1 == 'Preußen-Münster'):
        equipo_1 = 'preussen-muenster'
    elif (equipo_1 in ['Belgrano','Chacarita-Juniors','Huracan-de-Corrientes','Deportivo-Italiano']):
        continue


    url = 'https://www.livefutbol.com/equipos/'+equipo_1+'/9/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    eq = soup.find_all('div', class_='data')
    print('primerfor '+url)
    for x in (eq[1].table.find_all('tr')):
        if contador != False:
            tag = x.find_all('td')
            club.append(equipos2[equipo])
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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_primera_division_argentina',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)