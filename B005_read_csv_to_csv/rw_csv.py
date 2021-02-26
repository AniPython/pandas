import pandas as pd

df = pd.DataFrame(
    {
        '一': [1, 2],
        '二': [3, 4],
    }
)
print(df)
df.to_csv('tb1.csv', index=False, encoding='GBK')

df = pd.read_csv('tb1.csv', encoding='GBK')
print(df)
