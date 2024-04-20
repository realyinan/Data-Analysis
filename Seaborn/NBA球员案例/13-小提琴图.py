import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')
data_team2 = data[data['TEAM'].isin(['GS', 'CLE', 'SA', 'LAC', 'OKC', 'UTAH', 'CHA', 'TOR', 'NO', 'BOS'])]

sns.set_style('darkgrid')
plt.figure(figsize=(20, 10), dpi=70)

plt.subplot(3, 1, 1)
sns.violinplot(x='TEAM', y='3P%', data=data_team2)

plt.subplot(3, 1, 2)
sns.violinplot(x='TEAM', y='eFG%', data=data_team2)

plt.subplot(3, 1, 3)
sns.violinplot(x='TEAM', y='POINTS', data=data_team2)

plt.show()