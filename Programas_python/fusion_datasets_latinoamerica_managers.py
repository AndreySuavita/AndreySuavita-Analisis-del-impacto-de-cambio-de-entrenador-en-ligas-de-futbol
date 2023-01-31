import pandas as pd
import numpy as np

entrenadores_betplay_dimayor= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_betplay_dimayor")
entrenadores_brasileirao= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_brasileirao")
entrenadores_primera_division_argentina= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/managers/entrenadores_primera_division_argentina")

# agregar ligas a los datasets
largo=len(entrenadores_betplay_dimayor)
liga=['betplay_dimayor']*largo
entrenadores_betplay_dimayor['liga'] = liga

largo=len(entrenadores_brasileirao)
liga=['brasileirao']*largo
entrenadores_brasileirao['liga'] = liga

largo=len(entrenadores_primera_division_argentina)
liga=['primera_division_argentina']*largo
entrenadores_primera_division_argentina['liga'] = liga

df = pd.concat([entrenadores_betplay_dimayor, entrenadores_brasileirao ,entrenadores_primera_division_argentina], axis=0)

df.reset_index(drop = True, inplace = True) # reiniciar index

df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/managers/latinoamerica_managers',index=False)
print(df)
