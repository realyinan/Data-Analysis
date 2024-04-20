from matplotlib import pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# sns.barplot(x='day', y='total_bill', data=tips)
sns.pointplot(x='day', y='total_bill', data=tips)

plt.show()