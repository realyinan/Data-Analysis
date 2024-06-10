import pandas as pd


import pandas as pd

# 创建示例数据
data = {
    '性别': ['男', '女', '男', '女', '男', '女'],
    '喜欢的颜色': ['红', '蓝', '红', '红', '蓝', '蓝']
}

df = pd.DataFrame(data)

# 计算交叉表
交叉表 = pd.crosstab(df['性别'], df['喜欢的颜色'])

# 输出结果
print(交叉表)


# 计算频率交叉表
频率交叉表 = pd.crosstab(df['性别'], df['喜欢的颜色'], normalize=True)

# 输出结果
print(频率交叉表)


# 添加合计行和合计列
交叉表_带合计 = pd.crosstab(df['性别'], df['喜欢的颜色'], margins=True)

# 输出结果
print(交叉表_带合计)


# 创建更多示例数据
data = {
    '性别': ['男', '女', '男', '女', '男', '女'],
    '年龄组': ['青年', '中年', '青年', '中年', '老年', '青年'],
    '喜欢的颜色': ['红', '蓝', '红', '红', '蓝', '蓝']
}

df = pd.DataFrame(data)

# 使用多个因素计算交叉表
复杂交叉表 = pd.crosstab([df['性别'], df['年龄组']], df['喜欢的颜色'])

# 输出结果
print(复杂交叉表)
