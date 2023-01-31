import pandas as pd
import numpy as np

bundesliga_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/bundesliga_results")
eredivisie_paises_bajos_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/eredivisie_paises_bajos_results")
laliga_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/laliga_results")
ligue_1_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/ligue_1_results")
premier_league_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/premier_league_results")
primeira_liga_portugal_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/primeira_liga_portugal_results")
serie_a_italia_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/serie_a_italia_results")

# agregar ligas a los datasets
largo=len(bundesliga_results)
liga=['bundesliga']*largo
bundesliga_results['liga'] = liga

largo=len(eredivisie_paises_bajos_results)
liga=['eredivisie_paises_bajos']*largo
eredivisie_paises_bajos_results['liga'] = liga

largo=len(laliga_results)
liga=['laliga']*largo
laliga_results['liga'] = liga

largo=len(ligue_1_results)
liga=['ligue_1']*largo
ligue_1_results['liga'] = liga

largo=len(premier_league_results)
liga=['premier_league']*largo
premier_league_results['liga'] = liga

largo=len(primeira_liga_portugal_results)
liga=['primeira_liga_portugal']*largo
primeira_liga_portugal_results['liga'] = liga

largo=len(serie_a_italia_results)
liga=['serie_a_italia']*largo
serie_a_italia_results['liga'] = liga

df = pd.concat([bundesliga_results, eredivisie_paises_bajos_results ,laliga_results,ligue_1_results,premier_league_results,primeira_liga_portugal_results,serie_a_italia_results], axis=0)

df.reset_index(drop = True, inplace = True) # reiniciar index

df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results/europa_results',index=False)
print(df)
