import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.DataFrame({'x': np.random.randn(500), 'y': np.random.randn(500)})

sns.jointplot(x = 'x', y = 'y', data=df, kind='hex', color='r', ratio=8, space=1)

plt.show()