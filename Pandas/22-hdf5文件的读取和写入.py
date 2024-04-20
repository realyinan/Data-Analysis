import pandas as pd

# HDF5文件的读取和存储需要指定一个键，值为要存储的DataFrame
data = pd.read_hdf('Pandas\data\day_close.h5')
print(data.head())
data.to_hdf(r'Pandas\data\test.h5', key='day_close')
data1 = pd.read_hdf(r'Pandas\data\test.h5', key='day_close')
print(data1.head())