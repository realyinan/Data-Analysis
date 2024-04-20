import pandas as pd
import numpy as np

wis = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
wis = wis.replace(to_replace='?', value=np.nan)
wis = wis.dropna()
print(np.all(pd.notnull(wis)))
