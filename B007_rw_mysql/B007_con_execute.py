from sqlalchemy import create_engine


con = create_engine(
    "mysql+pymysql://root:admin123@localhost/sales2020"
)

# con.execute("insert into jd values ('aaa','2020-01-10',100)")
# con.execute("delete from jd where volume=100")
# con.execute("update jd set volume=1000 where goods_id='UQNA9200'")

con.execute("update school.students set 成绩=10 where id=1")
