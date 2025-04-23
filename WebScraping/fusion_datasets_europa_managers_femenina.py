import pandas as pd
import numpy as np

entrenadores_bundesliga_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_bundesliga_femenina")
entrenadores_damallsvenskan_suecia_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_damallsvenskan_suecia_femenina")
entrenadores_eredivisie_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_eredivisie_femenina")
entrenadores_laliga_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_laliga_femenina")
entrenadores_ligue_1_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_ligue_1_femenina")
entrenadores_mex_primera_division_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_mex_primera_division_femenina")
entrenadores_national_women_soccer_league_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_national_women_soccer_league_femenina")
entrenadores_premier_league_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_premier_league_femenina")
entrenadores_toppserien_noruega_femenina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/entrenadores_toppserien_noruega_femenina")

# agregar ligas a los datasets
largo=len(entrenadores_bundesliga_femenina)
liga=['bundesliga_femenina']*largo
entrenadores_bundesliga_femenina['liga'] = liga

largo=len(entrenadores_damallsvenskan_suecia_femenina)
liga=['damallsvenskan_sua_femenina']*largo
entrenadores_damallsvenskan_suecia_femenina['liga'] = liga

largo=len(entrenadores_eredivisie_femenina)
liga=['eredivisie_paises_bajos_femenina']*largo
entrenadores_eredivisie_femenina['liga'] = liga

largo=len(entrenadores_laliga_femenina)
liga=['laliga_femenina']*largo
entrenadores_laliga_femenina['liga'] = liga

largo=len(entrenadores_ligue_1_femenina)
liga=['ligue_1_femenina']*largo
entrenadores_ligue_1_femenina['liga'] = liga

largo=len(entrenadores_mex_primera_division_femenina)
liga=['mex_primera_division_femenina']*largo
entrenadores_mex_primera_division_femenina['liga'] = liga

largo=len(entrenadores_national_women_soccer_league_femenina)
liga=['national_women_soccer_league_femenina']*largo
entrenadores_national_women_soccer_league_femenina['liga'] = liga

largo=len(entrenadores_premier_league_femenina)
liga=['premier_league_femenina']*largo
entrenadores_premier_league_femenina['liga'] = liga

largo=len(entrenadores_toppserien_noruega_femenina)
liga=['toppserien_noruega_femenina']*largo
entrenadores_toppserien_noruega_femenina['liga'] = liga

df = pd.concat([entrenadores_bundesliga_femenina,entrenadores_damallsvenskan_suecia_femenina, entrenadores_eredivisie_femenina ,
                entrenadores_laliga_femenina,entrenadores_ligue_1_femenina,entrenadores_mex_primera_division_femenina,
                entrenadores_national_women_soccer_league_femenina,entrenadores_premier_league_femenina,entrenadores_toppserien_noruega_femenina], axis=0)

df.reset_index(drop = True, inplace = True) # reiniciar index

df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers_f/europa_managers_femenina',index=False)
print(df)
