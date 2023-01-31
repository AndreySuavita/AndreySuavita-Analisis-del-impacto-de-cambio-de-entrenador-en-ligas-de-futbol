from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Sporting CP', 'FC Arouca', 'Moreirense FC', 'CS Marítimo',
       'CD Tondela', 'Vitória Guimarães', 'Oporto', 'Paços de Ferreira',
       'Gil Vicente', 'GD Estoril', 'FC Vizela', 'Benfica',
       'Sporting Braga', 'Portimonense SC', 'FC Famalicão',
       'CD Santa Clara', 'Boavista', 'Belenenses SAD', 'CD Nacional',
       'SC Farense', 'Rio Ave FC', 'Vitória Setúbal', 'CD Aves',
       'CD Feirense', 'GD Chaves', 'Os Belenenses', 'União da Madeira',
       'Académica de Coimbra', 'FC Penafiel', 'SC Olhanense',
       'SC Beira-Mar', 'União Leiria', 'Naval 1° de Maio', 'Leixões SC',
       'Estrela Amadora', 'CD Trofense', 'FC Alverca', 'Varzim SC',
       'SC Salgueiros', 'Campomaiorense', 'Leça FC', 'SC Espinho',
       'FC Felgueiras 1932', 'FC Tirsense', 'União Torreense', 'AD Fafe',
       'Académico de Viseu', 'O Elvas', 'Sporting Covilhã', 'R.D. Águeda',
       'GC Alcobaça', 'Amora FC', 'FC Barreirense', 'GD Riopele',
       'Montijo', 'Atlético CP', 'União Tomar', 'CD da CUF Barreiro',
       'Oriental de Lisboa', 'União Coimbra', 'AD Sanjoanense',
       'Lusitano GC', 'Seixal', 'Caldas SC']
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
    elif (equipo_1 == 'CS-Marítimo'):
        equipo_1 = 'cs-maritimo'
    elif (equipo_1 == 'Vitória-Guimarães'):
        equipo_1 = 'cs-maritimo'
    elif (equipo_1 == 'Oporto'):
        equipo_1 = 'fc-porto'
    elif (equipo_1 == 'Paços-de-Ferreira'):
        equipo_1 = 'pacos-de-ferreira'
    elif (equipo_1 == 'Benfica'):
        equipo_1 = 'sl-benfica'
    elif (equipo_1 == 'FC-Famalicão'):
        equipo_1 = 'fc-famalicao'
    elif (equipo_1 == 'Vitória-Setúbal'):
        equipo_1 = 'vitoria-setubal'
    elif (equipo_1 == 'União-da-Madeira'):
        equipo_1 = 'uniao-da-madeira'
    elif (equipo_1 == 'Académica-de-Coimbra'):
        equipo_1 = 'academica-de-coimbra'
    elif (equipo_1 == 'União-Leiria'):
        equipo_1 = 'uniao-leiria'
    elif (equipo_1 == 'Naval-1°-de-Maio'):
        equipo_1 = 'naval-1-de-maio'
    elif (equipo_1 == 'Leixões-SC'):
        equipo_1 = 'leixoes-sc'
    elif (equipo_1 == 'Leça-FC'):
        equipo_1 = 'leca-fc'
    elif (equipo_1 == 'União-Torreense'):
        equipo_1 = 'uniao-torreense'
    elif (equipo_1 == 'Académico-de-Viseu'):
        equipo_1 = 'academico-de-viseu'
    elif (equipo_1 == 'Sporting-Covilhã'):
        equipo_1 = 'sporting-covilha'
    elif (equipo_1 == 'R.D.-Águeda'):
        equipo_1 = 'r-d-agueda'
    elif (equipo_1 == 'GC-Alcobaça'):
        continue
    elif (equipo_1 == 'GD-Riopele'):
        continue
    elif (equipo_1 == 'Montijo'):
        continue
    elif (equipo_1 == 'Atlético-CP'):
        equipo_1 = 'atletico-cp'
    elif (equipo_1 == 'União-Tomar'):
        continue
    elif (equipo_1 == 'CD-da-CUF-Barreiro'):
        equipo_1 = 'fabril-do-barreiro'
    elif (equipo_1 == 'União-Coimbra'):
        equipo_1 = 'uniao-coimbra'



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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_primeira_liga',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)