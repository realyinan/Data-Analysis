import pandas as pd

data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                    'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})

data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})
print(data1)
print(data2)
print('------------------------------------------------------')
inner = pd.merge(data1, data2, on=['key1', 'key2'])
print(inner)
print('------------------------------------------------------')
left = pd.merge(data1, data2, how='left', on=['key1', 'key2'])
print(left)
print('------------------------------------------------------')
right = pd.merge(data1, data2, how='right', on=['key1', 'key2'])
print(right)
print('------------------------------------------------------')
outer = pd.merge(data1, data2, how='outer', on=['key1', 'key2'])
print(outer)