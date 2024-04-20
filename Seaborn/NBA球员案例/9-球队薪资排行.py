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

# data_team = data.groupby('TEAM').agg({'SALARY_MILLIONS':np.mean})
data_team = data.groupby(['TEAM'])['SALARY_MILLIONS'].mean()

print(data_team.sort_values(ascending=False).head(10))