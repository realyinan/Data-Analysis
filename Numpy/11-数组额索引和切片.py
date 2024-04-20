import numpy as np

stock_change = np.random.normal(0, 1, (4, 5))
print(stock_change)

# 二位数组索引切片
# 举例：获取第一个股票的前3个交易日的涨跌幅数据
print(stock_change[0, 0:3])

# 三维数组索引切片
a1 = np.array(
    [ [[1,2,3],
       [4,5,6]], 
      [[12,3,34],
       [5,6,7]]
    ])
print(a1[1, 0, 0])