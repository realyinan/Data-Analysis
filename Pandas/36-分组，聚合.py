import pandas as pd

col =pd.DataFrame({'color': ['white','red','green','red','green'], 
                   'object': ['pen','pencil','pencil','ashtray','pen'],
                   'price1':[5.56,4.20,1.30,0.56,2.75],
                   'price2':[4.75,4.12,1.60,0.75,3.15]})
print(col)
print('--------------------------------------------------------------')
# 分组，求平均值（聚合）
print(col.groupby(['color'], as_index=False)['price1'].mean())
print(col['price1'].groupby(col['color']).mean())
