import numpy as np
import pandas as pd

# DataFrame是一个类似于二维数组或表格(如excel)的对象，既有行索引，又有列索引
a = pd.DataFrame(np.random.randn(2, 3))
print(a)
print('--------------------------------')
score = np.random.randint(40, 100, (10, 5))
score_df = pd.DataFrame(score)
subjects = ["语文", "数学", "英语", "政治", "体育"]
stu = ['学生'+str(i) for i in range(score_df.shape[0])]
data = pd.DataFrame(score, index=stu, columns=subjects)
print(data)
