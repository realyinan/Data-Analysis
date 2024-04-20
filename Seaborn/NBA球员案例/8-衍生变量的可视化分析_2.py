import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')

# 以年龄进行划分
def age_cut(df):
    if df['AGE'] <= 24:
        return 'young'
    elif df['AGE'] >= 30:
        return 'old'
    else:
        return 'best' 
    
data['age_cut'] = data.apply(lambda x: age_cut(x), axis=1)

sns.set_style('dark')

multi_data = data.loc[:, ['RPM','POINTS','TRB','AST','STL','BLK','age_cut']]
sns.pairplot(multi_data, hue='age_cut')

plt.show()