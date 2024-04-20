import numpy as np

stock_change = np.random.uniform(0, 1, (4, 5))
print(stock_change.astype(np.int64))
print('------------------------------------')

a1 = np.array(
    [ [[1,2,3],
       [4,5,6]], 
      [[12,3,34],
       [5,6,7]]
    ])
print(a1.tobytes())
