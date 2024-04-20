import pandas as pd
import numpy as np

score = np.random.randint(40, 100, (10, 5))
score_df = pd.DataFrame(score)
subjects = ["语文", "数学", "英语", "政治", "体育"]
stu = ['学生'+str(i) for i in range(score_df.shape[0])]
data = pd.DataFrame(score, index=stu, columns=subjects)
print(data)

# 修改行索引
stu = ['学生_'+str(i) for i in range(score_df.shape[0])]
data.index = stu
print(data)

# 重设索引
# reset_index(drop=False)
# 设置新的下标索引
# drop:默认为False，不删除原来索引，如果为True,删除原来的索引值
print(data.reset_index(drop=True))
 