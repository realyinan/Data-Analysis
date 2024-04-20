import pandas as pd
import numpy as np

score = np.random.randint(40, 100, (10, 5))
score_df = pd.DataFrame(score)
subjects = ["语文", "数学", "英语", "政治", "体育"]
stu = ['学生'+str(i) for i in range(score_df.shape[0])]
data = pd.DataFrame(score, index=stu, columns=subjects)
print(data)

print(data.shape)
print(data.index)
print(data.columns)
print(data.values)
print(data.head(5))
print(data.tail(5))
print(data.T)