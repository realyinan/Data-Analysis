import pandas as pd

# 创建示例数据框
data = {
    '姓名': ['张三', '李四', '张三', '王五'],
    '年龄': [25, 30, 25, 35],
    '城市': ['北京', '上海', '北京', '广州']
}

df = pd.DataFrame(data)

# 去除重复行
df_去重 = df.drop_duplicates()

# 输出结果
print("去除重复行后的数据框：")
print(df_去重)

# 根据 '姓名' 列去重
df_姓名去重 = df.drop_duplicates(subset=['姓名'])

# 输出结果
print("根据 '姓名' 列去重后的数据框：")
print(df_姓名去重)

# 保留最后出现的重复值
df_保留最后 = df.drop_duplicates(keep='last')

# 输出结果
print("保留最后出现的重复值后的数据框：")
print(df_保留最后)


# 删除所有重复值
df_删除所有重复 = df.drop_duplicates(keep=False)

# 输出结果
print("删除所有重复值后的数据框：")
print(df_删除所有重复)
