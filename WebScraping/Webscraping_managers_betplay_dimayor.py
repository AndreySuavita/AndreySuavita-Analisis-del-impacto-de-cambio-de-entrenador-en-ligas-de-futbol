from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Unión Magdalena', 'Deportivo Pereira', 'Patriotas FC',
       'Envigado FC', 'Atlético Bucaramanga', 'Deportivo Cali',
       'Millonarios', 'La Equidad', 'Atlético Nacional',
       'Deportes Tolima', 'América de Cali', 'Alianza Petrolera',
       'Cortuluá', 'Deportivo Pasto', 'Once Caldas', 'Atlético Junior',
       'Rionegro Águilas Doradas', 'Independiente Medellín',
       'Jaguares de Córdoba', 'Santa Fe', 'Deportes Quindío',
       'Atlético Huila', 'Boyacá Chicó', 'Cúcuta Deportivo', 'Leones FC',
       'Tigres FC', 'Fortaleza FC', 'Águilas Pereira', 'Uniautónoma FC',
       'Itagüi Ditaires', 'Real Cartagena']
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
    elif (equipo_1 == 'Unión-Magdalena'):
        equipo_1 = 'Union-Magdalena'
    elif (equipo_1 == 'Atlético-Bucaramanga'):
        equipo_1 = 'Atletico-Bucaramanga'
    elif (equipo_1 == 'Atlético-Nacional'):
        equipo_1 = 'Atletico-Nacional'
    elif (equipo_1 == 'América-de-Cali'):
        equipo_1 = 'America-de-Cali'
    elif (equipo_1 == 'Cortuluá'):
        equipo_1 = 'Cortulua'
    elif (equipo_1 == 'Atlético-Junior'):
        equipo_1 = 'Atletico-Junior'
    elif (equipo_1 == 'Rionegro-Águilas-Doradas' or equipo_1 == 'Itagüi-Ditaires' or equipo_1 == 'Águilas-Pereira'):
        equipo_1 = 'Rionegro-Aguilas-Doradas'
    elif (equipo_1 == 'Independiente-Medellín'):
        equipo_1 = 'Independiente-Medellin'
    elif (equipo_1 == 'Jaguares-de-Córdoba'):
        equipo_1 = 'Jaguares-de-Cordoba'
    elif (equipo_1 == 'Deportes-Quindío'):
        equipo_1 = 'Deportes-Quindio'
    elif (equipo_1 == 'Atlético-Huila'):
        equipo_1 = 'Atletico-Huila'
    elif (equipo_1 == 'Boyacá-Chicó'):
        equipo_1 = 'Boyaca-Chico'
    elif (equipo_1 == 'Fortuna-Düsseldorf'):
        equipo_1 = 'fortuna-duesseldorf'
    elif (equipo_1 == 'Cúcuta-Deportivo'):
        equipo_1 = 'Cucuta-Deportivo'
    elif (equipo_1 == 'Uniautónoma-FC'):
        equipo_1 = 'Uniautonoma-FC'


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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_betplay_dimayor',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)