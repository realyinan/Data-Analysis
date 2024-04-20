import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')

data_team2 = data[data['TEAM'].isin(['GS', 'CLE', 'SA', 'LAC', 'OKC', 'UTAH', 'CHA', 'TOR', 'NO', 'BOS'])]

sns.set_style('whitegrid')
plt.figure(figsize=(20, 8), dpi=70)

plt.subplot(1, 3, 1)
sns.boxplot(x='TEAM', y='SALARY_MILLIONS', data=data_team2)

plt.subplot(1, 3, 2)
sns.boxplot(x='TEAM', y='AGE', data=data_team2)

plt.subplot(1, 3, 3)
sns.boxplot(x='TEAM', y='MPG', data=data_team2)

plt.show()