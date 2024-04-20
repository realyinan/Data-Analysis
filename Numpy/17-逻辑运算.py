import numpy as np

# 生成10名同学，5门功课的数据
score = np.random.randint(40, 100, [10, 5])
print(score)

# 取出最后4名同学的成绩，用于逻辑判断
test_score = score[6:, :]
print(test_score > 60)

# BOOL赋值, 将满足条件的设置为指定的值-布尔索引
test_score[test_score > 60] = 1
print(test_score)