import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'

movie_name = ['雷神3: 诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']

x = range(len(movie_name))
y = [73853,57767,22354,15969,14839,8725,8716,8318,7916,6764,52222]

plt.figure(figsize=(20, 8), dpi=70)

plt.bar(x, y, width=0.5)

plt.xticks(x, movie_name)

plt.title('电影票房收入对比')

plt.grid(linestyle='--', alpha=0.5)

plt.show()
