import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(r'Seaborn\data\nba_2017_nba_players_with_salary.csv')

# 绘图来分别看一下球员薪水、效率值、年龄这三个信息的分布情况
plt.figure(figsize=(20, 8), dpi=70)

plt.subplot(1, 3, 1)
plt.hist(data['SALARY_MILLIONS'])
plt.title('Salary')
plt.grid()

plt.subplot(1, 3, 2)
plt.hist(data['RPM'])
plt.title('RPM')
plt.grid()

plt.subplot(1, 3, 3)
plt.hist(data['AGE'])
plt.title('Age')
plt.grid()

plt.show()