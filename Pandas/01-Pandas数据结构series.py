import pandas as pd
import numpy as np

# Series是一个类似于一维数组的数据结构，它能够保存任何类型的数据，比如整数、字符串、浮点数等，主要由一组数据和与之相关的索引两部分构成
print(pd.Series(np.arange(10)))

print(pd.Series([1.2, 2.3, 3.5, 3.9, 6.8], index=[1, 2, 3, 4, 5]))

color_count = pd.Series({'red':100, 'green':200, 'blue':256, 'yellow':750})
print(color_count)