"""
链式索引: chained indexing
链式赋值: chained_assignment
"""
import pandas as pd
import numpy as np

df = pd.DataFrame([
    [1, 4],
    [2, 5],
    [3, 6],
], columns=['A', 'B'])
print('df 0****')
print(df)

# 1 我想改变 df
# 1.1 出现 SettingWithCopyWarning
df.loc[df['A'] < 3]['B'] = 100
df.loc[df['A'] < 3].loc[:, 'B'] = 100
print('df 1.1****')
print(df)

# 1.2 解决
df.loc[df['A'] < 3, 'B'] = 100
print('df 1.2****')
print(df)

# 2 不想改变df, 想改df1
# 2 出现 SettingWithCopyWarning
df1 = df.loc[df['A'] < 3]
# df1 = df.loc[:, :]
# df1 = df.copy(deep=True)
print(df1)
pass
df1['B'] = 100
print(df1)
print(df)
print('df 2****')
print(df)
print(df1)

# 2 解决
df1 = df.loc[df['A'] < 3].copy()
df1['B'] = 100
print(df1)
print(df)

# 3 多层索引

dfmi = pd.DataFrame(
    [list('abcd'),
     list('efgh'),
     list('ijkl'),
     list('mnop')],
    columns=pd.MultiIndex.from_product([['one', 'two'],
                                        ['first', 'second']]))
print(dfmi)
dfmi['one']['second'] = 'x'
print(dfmi)

# 3 解决
dfmi[('one', 'second')] = 'xxx'
print(dfmi)
