import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.sin(x)

plt.figure(figsize=(20, 8), dpi=70)

plt.plot(x, y)

plt.grid()

plt.show()