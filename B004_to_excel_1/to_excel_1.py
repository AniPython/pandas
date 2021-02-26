import pandas as pd

df = pd.DataFrame({
    '销量': [10, 20],
    '售价': [100.123, None],
}, index=['aaa', 'bbb'])
df.index.name = '货号'
print(df)
# df.to_excel('tb_.xlsx',
#             sheet_name='tb1',
#             float_format='%.2f',
#             na_rep='我是空值')

df.to_excel('tb__.xlsx', index=False)
