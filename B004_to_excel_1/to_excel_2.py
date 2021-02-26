import pandas as pd
from datetime import datetime

df1 = pd.DataFrame(
    {'日期': [datetime(2020, 1, 1), datetime(2020, 1, 2)],
     '销量': [10, 20]}
)

df2 = pd.DataFrame(
    {'日期': [datetime(2020, 2, 1), datetime(2020, 2, 2)],
     '销量': [15, 25]}
)

print(df1)
print(df2)

with pd.ExcelWriter('tb.xlsx',
                    datetime_format='YYYY-MM-DD'
                    ) as writer:
    df1.to_excel(writer, sheet_name='1月')
    df2.to_excel(writer, sheet_name='2月')
