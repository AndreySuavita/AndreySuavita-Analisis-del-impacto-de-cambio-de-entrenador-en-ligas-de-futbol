from bs4 import BeautifulSoup
import requests
import pandas as pd

equipos=['Fluminense RJ', 'Atlético Goianiense', 'Palmeiras',
       'Coritiba - PR', 'Atlético Mineiro', 'Botafogo - RJ', 'Fortaleza',
       'Avaí - SC', 'São Paulo FC', 'Juventude - RS', 'Goiás - GO',
       'América - MG', 'Corinthians SP', 'Cuiabá - MT', 'Santos FC',
       'Flamengo RJ', 'Athletico Paranaense', 'Red Bull Bragantino',
       'Internacional', 'Ceará - CE', 'Bahia - BA', 'Chapecoense',
       'Sport - PE', 'Grêmio Porto Alegre', 'Vasco da Gama - RJ',
       'CSA - AL', 'Cruzeiro', 'Vitória - BA', 'Paraná Clube',
       'Ponte Preta', 'Santa Cruz - PE', 'Figueirense - SC',
       'Joinville - SC', 'Criciúma - SC', 'Náutico - PE',
       'Portuguesa - SP', 'Guarani - SP', 'Grêmio Prudente',
       'Santo André - SP', 'Grêmio Barueri - SP', 'Ipatinga FC',
       'América - RN', 'São Caetano - SP', 'Brasiliense - DF',
       'Paysandu - PA', 'Gama - DF', 'Botafogo - SP', 'Anapolina - GO',
       'River - PI', 'Remo - PA', 'São Raimundo - AM',
       'Desportiva Ferroviária - ES', 'Sampaio Corrêa - MA', 'Serra - ES',
       'Vila Nova - GO', 'ABC - RN', 'União Bandeirante - PR',
       'CR Brasil - AL', 'Nacional - AM', 'Bangu - RJ',
       'XV de Piracicaba - SP', 'Caxias - SC', 'Brasil de Pelotas - RS',
       'América - RJ', 'Villa Nova - MG', 'União São João - SP',
       'Marcílio Dias - SC', 'Londrina - PR', 'Americano - RJ',
       'CA Bragantino']
equipos2=['Fluminense RJ', 'Atlético Goianiense', 'Palmeiras',
       'Coritiba - PR', 'Atlético Mineiro', 'Botafogo - RJ', 'Fortaleza',
       'Avaí - SC', 'São Paulo FC', 'Juventude - RS', 'Goiás - GO',
       'América - MG', 'Corinthians SP', 'Cuiabá - MT', 'Santos FC',
       'Flamengo RJ', 'Athletico Paranaense', 'Red Bull Bragantino',
       'Internacional', 'Ceará - CE', 'Bahia - BA', 'Chapecoense',
       'Sport - PE', 'Grêmio Porto Alegre', 'Vasco da Gama - RJ',
       'CSA - AL', 'Cruzeiro', 'Vitória - BA', 'Paraná Clube',
       'Ponte Preta', 'Santa Cruz - PE', 'Figueirense - SC',
       'Joinville - SC', 'Criciúma - SC', 'Náutico - PE',
       'Portuguesa - SP', 'Guarani - SP', 'Grêmio Prudente',
       'Santo André - SP', 'Grêmio Barueri - SP', 'Ipatinga FC',
       'América - RN', 'São Caetano - SP', 'Brasiliense - DF',
       'Paysandu - PA', 'Gama - DF', 'Botafogo - SP', 'Anapolina - GO',
       'River - PI', 'Remo - PA', 'São Raimundo - AM',
       'Desportiva Ferroviária - ES', 'Sampaio Corrêa - MA', 'Serra - ES',
       'Vila Nova - GO', 'ABC - RN', 'União Bandeirante - PR',
       'CR Brasil - AL', 'Nacional - AM', 'Bangu - RJ',
       'XV de Piracicaba - SP', 'Caxias - SC', 'Brasil de Pelotas - RS',
       'América - RJ', 'Villa Nova - MG', 'União São João - SP',
       'Marcílio Dias - SC', 'Londrina - PR', 'Americano - RJ',
       'CA Bragantino']
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
    elif (equipo_1 == 'Gremio-Prudente'):
        equipo_1 = 'gremio-barueri-sp'
    elif (equipo_1 == 'Ipatinga-FC'):
        equipo_1 = 'ipatinga-mg'
    elif (equipo_1 == 'CA-Bragantino'):
        equipo_1 = 'red-bull-bragantino'
    elif (equipo_1 in['Palmeiras','SV-Bayer-04-Leverkusen','Anapolina-GO','River-PI','Sao-Raimundo-AM','Desportiva-Ferroviaria-ES',
                      'Serra-ES','Uniao-Bandeirante-PR','Nacional-AM','Caxias-SC']):
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
df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_brasileirao',index=False)
#df.to_csv('Premier_league_liverpool_managers',index=False)

print(df)