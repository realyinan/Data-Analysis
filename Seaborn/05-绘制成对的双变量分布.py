import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

dataset = sns.load_dataset('iris')

sns.pairplot(dataset)

plt.show()