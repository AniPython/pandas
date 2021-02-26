import pandas as pd
from sqlalchemy import create_engine

con = create_engine(
    "mysql+pymysql://root:admin123@localhost/sales2020"
)

# 1: 传入表名
df = pd.read_sql('jd', con=con,
                 columns=['goods_id', 'volume'])
print(df)


# 2: 传入sql查询语句
df = pd.read_sql(
    'select goods_id,volume from jd where volume > 5 order by volume',
    con=con)
print(df)
