import pandas as pd
import numpy as np

betplay_dimayor_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/betplay_dimayor_results")
brasileirao_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/brasileirao_results")
primera_division_argentina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/primera_division_argentina_results")

# agregar ligas a los datasets
largo=len(betplay_dimayor_results)
liga=['betplay_dimayor']*largo
betplay_dimayor_results['liga'] = liga

largo=len(brasileirao_results)
liga=['brasileirao']*largo
brasileirao_results['liga'] = liga

largo=len(primera_division_argentina_results)
liga=['primera_division_argentina']*largo
primera_division_argentina_results['liga'] = liga

df = pd.concat([betplay_dimayor_results, brasileirao_results ,primera_division_argentina_results], axis=0)

df.reset_index(drop = True, inplace = True) # reiniciar index

df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/latinoamerica_results',index=False)
print(df)
