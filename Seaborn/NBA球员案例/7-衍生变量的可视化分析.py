import pandas as pd
import numpy as np
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

sns.set_style('darkgrid')
plt.figure(figsize=(10, 10), dpi=70)


x1 = data[data['age_cut'] == 'best'].SALARY_MILLIONS
y1 = data[data['age_cut'] == 'best'].RPM
plt.plot(x1, y1, '^', label='best')

x2 = data[data['age_cut'] == 'young'].SALARY_MILLIONS
y2 = data[data['age_cut'] == 'young'].RPM
plt.plot(x2, y2, '^', label='young')

x3 = data[data['age_cut'] == 'old'].SALARY_MILLIONS
y3 = data[data['age_cut'] == 'old'].RPM
plt.plot(x3, y3, '^', label='old')

plt.legend(loc='best')
plt.title('RPM and SALARY')
plt.show()
