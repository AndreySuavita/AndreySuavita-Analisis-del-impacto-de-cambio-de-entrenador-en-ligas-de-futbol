import pandas as pd
import numpy as np

entrenadores_bundesliga= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_bundesliga")
entrenadores_eredivisie= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_eredivisie")
entrenadores_laliga= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_laliga")
entrenadores_ligue_1= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_ligue_1")
entrenadores_premier_league= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_premier_league")
entrenadores_primeira_liga= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_primeira_liga")
entrenadores_serie_a= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_serie_a")

# agregar ligas a los datasets
largo=len(entrenadores_bundesliga)
liga=['bundesliga']*largo
entrenadores_bundesliga['liga'] = liga

largo=len(entrenadores_eredivisie)
liga=['eredivisie_paises_bajos']*largo
entrenadores_eredivisie['liga'] = liga

largo=len(entrenadores_laliga)
liga=['laliga']*largo
entrenadores_laliga['liga'] = liga

largo=len(entrenadores_ligue_1)
liga=['ligue_1']*largo
entrenadores_ligue_1['liga'] = liga

largo=len(entrenadores_premier_league)
liga=['premier_league']*largo
entrenadores_premier_league['liga'] = liga

largo=len(entrenadores_primeira_liga)
liga=['primeira_liga_portugal']*largo
entrenadores_primeira_liga['liga'] = liga

largo=len(entrenadores_serie_a)
liga=['serie_a_italia']*largo
entrenadores_serie_a['liga'] = liga


df = pd.concat([entrenadores_bundesliga, entrenadores_eredivisie ,entrenadores_laliga,entrenadores_ligue_1,entrenadores_premier_league,entrenadores_primeira_liga,entrenadores_serie_a], axis=0)

df.reset_index(drop = True, inplace = True) # reiniciar index

df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/europa_managers',index=False)
print(df)

