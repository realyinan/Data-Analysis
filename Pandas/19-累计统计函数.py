import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('Pandas\data\stock_day.csv')
data = data.sort_index()
stock_change = data['price_change']
print(stock_change.cumsum())
# plot方法集成了前面直方图、条形图、饼图、折线图
stock_change.cumsum().plot()
plt.show()

 