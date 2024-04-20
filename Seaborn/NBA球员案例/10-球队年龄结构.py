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

# 按照分球队分年龄段，上榜球员降序排列，如上榜球员数相同，则按效率值降序排列。
data_team = data.groupby(['TEAM', 'age_cut'], as_index=False).agg({'SALARY_MILLIONS':np.mean, 'RPM':np.mean, 'PLAYER':np.size})
print(data_team.sort_values(by=['PLAYER', 'RPM'], ascending=False))