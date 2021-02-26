import pandas as pd
from sqlalchemy import create_engine


con = create_engine(
    "mysql+pymysql://root:admin123@localhost/sales2020"
)

df = pd.read_excel('jd.xlsx')
print(df)

df = df.rename(columns={
    '货号': 'goods_id',
    '日期': 'date',
    '销量': 'volume',
})
print(df)

df.to_sql('jd', con=con,
          index=False, if_exists='append')

