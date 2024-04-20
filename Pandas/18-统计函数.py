import pandas as pd

data = pd.read_csv('Pandas\data\stock_day.csv')

# 对于单个函数去进行统计的时候，坐标轴还是按照默认列“columns” (axis=0, default)，如果要对行“index” 需要指定(axis=1)
print(data.max(0))
print(data.std())
# 求出最大值的位置
print(data.idxmax())
print(data.idxmin())

df = pd.DataFrame({'COL1' : [2,3,4,5,4,2],
                   'COL2' : [0,1,2,3,4,2]})

print(df.median())