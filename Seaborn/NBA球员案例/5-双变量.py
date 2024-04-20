import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')

sns.set_style('darkgrid')

sns.jointplot(x = data['AGE'], y = data['SALARY_MILLIONS'], data=data, kind='hex')

plt.show()