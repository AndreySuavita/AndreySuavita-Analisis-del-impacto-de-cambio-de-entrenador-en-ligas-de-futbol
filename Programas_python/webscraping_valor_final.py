from bs4 import BeautifulSoup
import requests
import pandas as pd

lista_arreglar_resultado=[]
for x in list(range(0, 30)):
    for y in list(range(0, 30)):
        lista_arreglar_resultado.append(' ' + '(' + str(x) + ':' + str(y) + ')')


## para finales
url='https://www.livefutbol.com/calendario/col-primera-a-2020-liguilla-de-eliminados-halbfinale/0/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser' )
eq = soup.find_all('div',class_='data')

#print(len(eq[2].table.find_all('tr')))
#print(eq[2].table.find_all('tr')[3])
#print(len(eq[2].table.find_all('tr')[3].find_all('td')))
#print(eq[2].table.find_all('tr')[3].find_all('td'))
jornada_lista=[]
local=[]
visitante=[]
goles_local=[]
goles_visitante=[]
fecha=[]
contador = 0
for x in (eq[2].table.find_all('tr')):
  contador = contador +1
  if contador == 4:
    break
  if contador > 2:
    tag = x.find_all('td')
    jornada_lista.append("final")
    for y in list(range(0, 4)):
      if y == 1 or y == 3:
        #fecha
        z = tag[y].text
        z = z.replace('I: ', '')
        z = z.replace('V: ', '')
        z = z.split(' ')
        z = z[0]
        z = z.replace('.', '-')
        fecha.append(z)
  else:
    tag = x.find_all('td')
    jornada_lista.append("final")
    for y in list(range(0, 5)):
      # local
      if y == 1:
        z = tag[y].text
        z = z.replace('\n', '')
        local.append(z)
      # visitante
      elif y == 3:
        z = tag[y].text
        z = z.replace('\n', '')
        visitante.append(z)
      # goles
      elif y == 4:
        z = tag[y].text
        z = z.replace('\n', '')

        # for para quitar los resultados de medio tiempo
        for posibilidad in lista_arreglar_resultado:
          z = z.replace(posibilidad, '')
        z_lista = z.split(':')
        if (
                z == '-:- ' or z == '-:-  ' or z == ' -:- ' or z == ' no jug. ' or z == 'no jug. ' or z == ' no jug.' or z == ' apla.' or z == 'apla. ' or z == ' susp.'):
          goles_local.append(None)
          goles_visitante.append(None)
        else:
          goles_local.append(int(float(z_lista[0])))
          goles_visitante.append(int(float(z_lista[1])))
      else:
        continue

print("fecha.append("+"'"+str(fecha[0])+"'"+")\n"+"jornada_lista.append("+"'"+str(jornada_lista[0])+"'"+")\n"+"local.append("+"'"+str(local[0])+"'"+")\n"+"visitante.append("+"'"+str(visitante[0])+"'"+")\n"+ "goles_local.append("+"int("+str(goles_local[0])+"))\n"+"goles_visitante.append("+"int("+str(goles_visitante[0])+"))\n")
print("fecha.append("+"'"+str(fecha[1])+"'"+")\n"+"jornada_lista.append("+"'"+str(jornada_lista[1])+"'"+")\n"+"local.append("+"'"+str(local[1])+"'"+")\n"+"visitante.append("+"'"+str(visitante[1])+"'"+")\n"+ "goles_local.append("+"int("+str(goles_local[1])+"))\n"+"goles_visitante.append("+"int("+str(goles_visitante[1])+"))\n")

#print(local,visitante,goles_local,goles_visitante,fecha)
