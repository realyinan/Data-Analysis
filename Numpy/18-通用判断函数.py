import numpy as np

# 生成10名同学，5门功课的数据
score = np.random.randint(40, 100, [10, 5])
print(score)

# 判断前两名同学的成绩[0:2, :]是否全及格
print(np.all(score[0:2]) > 60)
# 判断前两名同学的成绩[0:2, :]是否有大于90分的
print(np.any(score[0:2]) > 90)
print(score)