import pandas as pd
import numpy as np

data = pd.read_csv('Pandas/data/IMDB-Movie-Data.csv')
print(data)

for i in data.columns:
    if np.all(pd.notnull(data[i])) == False:
        print(i)
        data[i] = data[i].fillna(data[i].mean())
print(data)