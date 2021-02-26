"""
Python Pandas Excel 学习群: 1148295690
AAA009
SettingWithCopyWarning
pandas开发者: 我猜你不知道自己在做什么, 所以给你一个提示
chained indexing: 链式索引
chained assignment: 链式赋值
"""
import pandas as pd

df = pd.DataFrame([
    [1, 4],
    [2, 5],
    [3, 6],
], columns=['A', 'B'])
print(df)

# 1
df.loc[df['A'] < 3]['B'] = 100  # SettingWithCopyWarning
df.loc[df['A'] < 3].loc[:, 'B'] = 100  # SettingWithCopyWarning
# print(df)

# 1 解决
# df.loc[df['A'] < 3, 'B'] = 100
# print(df)

# 2
df1 = df.loc[df['A'] < 3]  # SettingWithCopyWarning
# df1 = df.loc[:, :]
# df1 = df.copy(deep=True)
# df1 = df.loc[df['A'] < 3].copy()  # 解决方法
# print(df1)
df1['B'] = 100  # SettingWithCopyWarning
# print(df1)
# print(df)


# 3
dfmi = pd.DataFrame(
    [list('abcd'),
     list('efgh'),
     list('ijkl'),
     list('mnop')],
    columns=pd.MultiIndex.from_product([['one', 'two'],
                                        ['first', 'second']]))
print(dfmi)

dfmi['one']['second'] = 'xxx'  # SettingWithCopyWarning
# print(dfmi)

dfmi[('one', 'second')] = 'xxx'  # 解决
print(dfmi)
