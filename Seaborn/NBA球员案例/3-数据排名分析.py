import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')

# 按照效率值排名
print(data.loc[:, ['PLAYER', 'RPM', 'AGE']].sort_values(by='RPM', ascending=False))

# 按照球员薪资排名
print(data.loc[:, ['PLAYER', 'RPM', 'AGE', 'SALARY_MILLIONS']].sort_values(by='SALARY_MILLIONS', ascending=False))