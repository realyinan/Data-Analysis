import pandas as pd
import numpy as np

data = pd.read_csv('Pandas\data\IMDB-Movie-Data.csv')
print(data)
data = data.dropna()
print(data)
print(np.all(pd.notnull(data)))