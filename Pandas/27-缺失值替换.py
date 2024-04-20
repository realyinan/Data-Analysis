import pandas as pd
import numpy as np

data = pd.read_csv('Pandas\data\IMDB-Movie-Data.csv')

print(data['Revenue (Millions)'].mean())
print(data['Revenue (Millions)'])
print(data['Revenue (Millions)'].fillna(data['Revenue (Millions)'].mean()))
print(data)

