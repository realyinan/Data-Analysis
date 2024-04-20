import random
import time
import numpy as np
a = []
for i in range(100000000):
    a.append(random.random())
# 查看当前行的代码运行一次所花费的时间
# start_time = time.time()
# sum1=sum(a)
# end_time = time.time()
# print(end_time - start_time)
b=np.array(a)
start_time = time.time()
sum2=np.sum(b)
end_time = time.time()
print(end_time - start_time)


