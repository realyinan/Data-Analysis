import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')

# 展示多个变量之间的关系

multi_data = data.loc[:, ['RPM','SALARY_MILLIONS','AGE','POINTS']]

sns.pairplot(multi_data, height=1.8, aspect=1)

plt.show()