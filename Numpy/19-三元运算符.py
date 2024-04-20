import numpy as np

score = np.random.randint(40, 100, [10, 5])

# 判断前四名学生,前四门课程中，成绩中大于60的置为1，否则为0
test_score = score[0:4, 0:4]
print(test_score)
print(np.where(test_score > 60, 1, 0))

# 复合逻辑需要结合np.logical_and和np.logical_or使用

# 判断前四名学生,前四门课程中，成绩中大于60且小于90的换为1，否则为0
print(np.where(np.logical_and(test_score > 60, test_score < 90), 1, 0))
# 判断前四名学生,前四门课程中，成绩中大于90或小于60的换为1，否则为0
print(np.where(np.logical_or(test_score > 90, test_score < 60), 1, 0))
