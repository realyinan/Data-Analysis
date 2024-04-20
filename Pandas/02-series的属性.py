import pandas as pd
import numpy as np

color_count = pd.Series({'red':100, 'green':200, 'blue':256, 'yellow':750})
print(color_count)
print(color_count.index)
print(color_count.values)
print(color_count['red'])