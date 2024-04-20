import pandas as pd

# pandas.read_json(path_or_buf=None, orient=None, typ='frame', lines=False)
# 将JSON格式准换成默认的Pandas DataFrame格式
# orient : string,Indication of expected JSON string format.
        # 'split' : dict like {index -> [index], columns -> [columns], data -> [values]}
        # split 将索引总结到索引，列名到列名，数据到数据。将三部分都分开了
        # 'records' : list like [{column -> value}, ... , {column -> value}]
        # records 以
        # columns：values 的形式输出
        # 'index' : dict like {index -> {column -> value}}
        # index 以
        # index：{columns：values}... 的形式输出
        # 'columns' : dict like {column -> {index -> value}},默认该格式
        # colums 以
        # columns:{index:values} 的形式输出
        # 'values' : just the values array
        # values 直接输出值
# lines : boolean, default False
# 按照每行读取json对象
# typ : default ‘frame’， 指定转换成的对象类型series或者dataframe
data = pd.read_json('Pandas\data\Sarcasm_Headlines_Dataset.json', orient='records', lines=True)
print(data)

# DataFrame.to_json(path_or_buf=None, orient=None, lines=False)
# 将Pandas 对象存储为json格式
# path_or_buf=None：文件地址
# orient:存储的json形式，{‘split’,’records’,’index’,’columns’,’values’}
# lines:一个对象存储为一行

data.to_json(r'Pandas\data\test1.json', orient='records')
data.to_json(r'Pandas\data\test2.json', orient='records', lines=True)
data_new = pd.read_json(r'Pandas\data\test1.json', orient='records', lines=True)
data_new1 = pd.read_json(r'Pandas\data\test2.json', orient='records', lines=True)

print(data_new)
print(data_new1)
