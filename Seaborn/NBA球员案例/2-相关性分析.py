import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')

data_cor = data.loc[:, ['RPM', 'AGE', 'SALARY_MILLIONS', 'ORB', 'DRB', 'TRB','AST', 'STL', 'BLK', 'TOV', 'PF', 'POINTS', 'GP', 'MPG', 'ORPM', 'DRPM']]

# 获取两列数据之间的相关性
corr = data_cor.corr()

plt.figure(figsize=(12, 8), dpi=70)

sns.heatmap(corr, square=True, linewidths=0.1, annot=True)

plt.show()
