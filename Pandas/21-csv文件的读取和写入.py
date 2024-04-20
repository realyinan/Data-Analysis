import pandas as pd

# pandas.read_csv(filepath_or_buffer, sep =',', usecols )
# filepath_or_buffer:文件路径
# sep :分隔符，默认用","隔开
# usecols:指定读取的列名，列表形式

data = pd.read_csv('Pandas\data\stock_day.csv', usecols=['open', 'close'])
print(data.head())

# DataFrame.to_csv(path_or_buf=None, sep=', ’, columns=None, header=True, index=True, mode='w', encoding=None)
# path_or_buf :文件路径
# sep :分隔符，默认用","隔开
# columns :选择需要的列索引
# header :boolean or list of string, default True,是否写进列索引值
# 115
# index:是否写进行索引
# mode:'w'：重写, 'a' 追加

data.to_csv(r'Pandas\data\test.csv', columns=['open'], index=False)
data1 = pd.read_csv(r'Pandas\data\test.csv')
print(data1)

