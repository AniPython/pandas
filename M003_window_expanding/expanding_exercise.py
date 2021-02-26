import pandas as pd

df = pd.read_excel('month_sales.xlsx')
df.dropna(subset=['销售额'], inplace=True)

df['累计销售额'] = df['销售额'].expanding().sum()
df['实际完成率'] = df['累计销售额'] / 120
df['目标完成率'] = [x/12 for x in range(1, len(df) + 1)]

df['t'] = df['销售额'].astype(str).str.len()

print(df)
# df.to_excel('tb.xlsx', index=False)
