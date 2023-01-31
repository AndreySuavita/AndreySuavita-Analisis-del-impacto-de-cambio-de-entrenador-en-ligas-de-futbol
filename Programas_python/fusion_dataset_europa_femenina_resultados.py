import pandas as pd
import numpy as np
import datetime
import time

partidos= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/europa_results_femenina")
entrenadores= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/europa_managers_femenina")


#Codigo para rellenar fechas faltantes
# funcion para detectar NaN o nan
def isNaN(num):
    return num != num

fecha_completar=""
for x in list(range(len(partidos))):
  if isNaN(partidos['fecha'][x]):
    partidos['fecha'][x] = fecha_completar
  else:
    fecha_completar = partidos['fecha'][x]
partidos.head(5)


# Codigo unir datasets partidos y entrenadores por medio de la fecha
entrenador_local = [None] * len(partidos)
pais_entrenador_local = [None] * len(partidos)

# Recorrer entrenadores
for entrenador in list(range(len(entrenadores))):
    print(entrenador)
    # for entrenador in list(range(2)):
    # Fecha entrenador inicio
    fecha_entrenador_inicio = (entrenadores['fecha_activo_inicio'][entrenador])
    fecha_entrenador_inicio_lista = fecha_entrenador_inicio.replace('-', '/')
    fecha_entrenador_inicio_formatted_date = time.strptime(fecha_entrenador_inicio_lista, "%d/%m/%Y")
    # Fecha  entrenador fin
    fecha_entrenador_fin = (entrenadores['fecha_activo_fin'][entrenador])
    fecha_entrenador_fin_lista = fecha_entrenador_fin.replace('-', '/')
    fecha_entrenador_fin_formatted_date = time.strptime(fecha_entrenador_fin_lista, "%d/%m/%Y")
    # Recorrer clubes
    for club in list(range(len(partidos))):
        # Comparar club del equipo con club del entrenador
        if partidos['local'][club] == entrenadores['club'][entrenador]:
            # Fecha club
            fecha_club = (partidos['fecha'][club])
            fecha_club_lista = fecha_club.replace('-', '/')
            fecha_club_formatted_date = time.strptime(fecha_club_lista, "%d/%m/%Y")
            # Comprovar si la fecha del equipo se encuentra en el rango de fechas del entrenador
            if fecha_club_formatted_date >= fecha_entrenador_inicio_formatted_date and fecha_club_formatted_date <= fecha_entrenador_fin_formatted_date:
                # asignar a la lista del entrenador en la posicion actual el valor del entrenador
                entrenador_local[club] = entrenadores['entrenador'][entrenador]
                pais_entrenador_local[club] = entrenadores['pais'][entrenador]

partidos['entrenador_local'] = entrenador_local
partidos['pais_entrenador_local'] = pais_entrenador_local
#################################################################
entrenador_visitante = [None] * len(partidos)
pais_entrenador_visitante = [None] * len(partidos)

# Recorrer entrenadores
for entrenador in list(range(len(entrenadores))):
    print(entrenador)
    # for entrenador in list(range(2)):
    # Fecha entrenador inicio
    fecha_entrenador_inicio = (entrenadores['fecha_activo_inicio'][entrenador])
    fecha_entrenador_inicio_lista = fecha_entrenador_inicio.replace('-', '/')
    fecha_entrenador_inicio_formatted_date = time.strptime(fecha_entrenador_inicio_lista, "%d/%m/%Y")
    # Fecha  entrenador fin
    fecha_entrenador_fin = (entrenadores['fecha_activo_fin'][entrenador])
    fecha_entrenador_fin_lista = fecha_entrenador_fin.replace('-', '/')
    fecha_entrenador_fin_formatted_date = time.strptime(fecha_entrenador_fin_lista, "%d/%m/%Y")
    # Recorrer clubes
    for club in list(range(len(partidos))):
        # Comparar club del equipo con club del entrenador
        if partidos['visitante'][club] == entrenadores['club'][entrenador]:
            # Fecha club
            fecha_club = (partidos['fecha'][club])
            fecha_club_lista = fecha_club.replace('-', '/')
            fecha_club_formatted_date = time.strptime(fecha_club_lista, "%d/%m/%Y")
            # Comprovar si la fecha del equipo se encuentra en el rango de fechas del entrenador
            if fecha_club_formatted_date >= fecha_entrenador_inicio_formatted_date and fecha_club_formatted_date <= fecha_entrenador_fin_formatted_date:
                # asignar a la lista del entrenador en la posicion actual el valor del entrenador
                entrenador_visitante[club] = entrenadores['entrenador'][entrenador]
                pais_entrenador_visitante[club] = entrenadores['pais'][entrenador]

partidos['entrenador_visitante'] = entrenador_visitante
partidos['pais_entrenador_visitante'] = pais_entrenador_visitante


#invertir index de "partidos"
#partidos['index'] = list(range(len(partidos)-1,-1,-1))
#partidos.set_index('index', inplace = True)
#partidos = partidos.sort_index()

partidos.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/datasets_unificados/europa_femenina_resultados.csv',index=False)
print(partidos)