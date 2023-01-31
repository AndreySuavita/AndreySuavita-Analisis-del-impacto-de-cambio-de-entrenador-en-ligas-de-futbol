import pandas as pd
import numpy as np

bundesliga_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/bundesliga_femenina_results")
damallsvenskan_suecia_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/damallsvenskan_suecia_femenina_results")
eredivisie_paises_bajos_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/eredivisie_paises_bajos_femenina_results")
laliga_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/laliga_femenina_results")
ligue_1_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/ligue_1_femenina_results")
mex_primera_division_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/mex_primera_division_femenina_results")
national_womens_soccer_league_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/national_womens_soccer_league_femenina_results")
premier_league_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/premier_league_femenina_results")
toppserien_noruega_femenina_results= pd.read_csv("D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/toppserien_noruega_femenina_results")

# agregar ligas a los datasets
largo=len(bundesliga_femenina_results)
liga=['bundesliga_femenina']*largo
bundesliga_femenina_results['liga'] = liga

largo=len(damallsvenskan_suecia_femenina_results)
liga=['damallsvenskan_suecia_femenina']*largo
damallsvenskan_suecia_femenina_results['liga'] = liga

largo=len(eredivisie_paises_bajos_femenina_results)
liga=['eredivisie_paises_bajos_femenina']*largo
eredivisie_paises_bajos_femenina_results['liga'] = liga

largo=len(laliga_femenina_results)
liga=['laliga_femenina']*largo
laliga_femenina_results['liga'] = liga

largo=len(ligue_1_femenina_results)
liga=['ligue_1_femenina']*largo
ligue_1_femenina_results['liga'] = liga

largo=len(mex_primera_division_femenina_results)
liga=['mex_primera_division_femenina']*largo
mex_primera_division_femenina_results['liga'] = liga

largo=len(national_womens_soccer_league_femenina_results)
liga=['national_womens_soccer_league_femenina']*largo
national_womens_soccer_league_femenina_results['liga'] = liga

largo=len(premier_league_femenina_results)
liga=['premier_league_femenina']*largo
premier_league_femenina_results['liga'] = liga

largo=len(toppserien_noruega_femenina_results)
liga=['toppserien_noruega_femenina']*largo
toppserien_noruega_femenina_results['liga'] = liga

df = pd.concat([bundesliga_femenina_results,damallsvenskan_suecia_femenina_results, eredivisie_paises_bajos_femenina_results 
                ,laliga_femenina_results,ligue_1_femenina_results,mex_primera_division_femenina_results,national_womens_soccer_league_femenina_results,
                premier_league_femenina_results,toppserien_noruega_femenina_results], axis=0)

df.reset_index(drop = True, inplace = True) # reiniciar index

df.to_csv('D:/MEGAsync/andrey u/Maestría/Tesis/datasets_results_f/europa_results_femenina',index=False)
print(df)
