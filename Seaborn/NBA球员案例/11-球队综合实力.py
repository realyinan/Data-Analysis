import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')

def age_cut(df):
    if df['AGE'] <= 24:
        return 'young'
    elif df['AGE'] >= 30:
        return 'old'
    else:
        return 'best' 
    
data['age_cut'] = data.apply(lambda x: age_cut(x), axis=1)

data_rpm2 = data.groupby(by=['TEAM'], as_index=False).agg({'SALARY_MILLIONS': np.mean,
                                                          'RPM': np.mean,
                                                          'PLAYER': np.size,
                                                          'POINTS': np.mean,
                                                          'eFG%': np.mean,
                                                          'MPG': np.mean,
                                                          'AGE': np.mean})

print(data_rpm2.head())
print(data_rpm2.sort_values(by="RPM", ascending=False).head())