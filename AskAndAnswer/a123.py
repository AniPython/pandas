import pandas as pd 

# df = pd.read_excel(r'C:\Users\Administrator\Desktop\3.xlsx')
df = pd.read_excel('AAA003.xlsx')
df = df.sort_values(['货号', '下单时间'])   #进行排序
df.index = range(len(df))   #索引重置
grouped_hp = df.groupby('货号')
m = grouped_hp.groups   #分组后给一个变量
new_lie = []   #新建一个空列表用来保存接下来的新的列对应的值
for n in m.values():   #遍历分组后的对象得到的是一个每个组对应的索引列表
    num = 0   #定义一个计数器
    for sy in n:   #遍历索引列表得到每一个索引
        if num == 0:   #判断如果分组的第一个那么现有尺码就是下单尺码
            c2 = df.loc[sy, '下单尺码']
            new_lie.append(c2)    #添加到之前创建的空列表
            num += 1   #计数器加一
        else:   #如果不是第一个先把前一天的现有尺码找出来，再加上今天的下单尺码，字符串拼接完成后拆分，建立集合，
        #集合是没有重复值的    再拼接起来，然后把拼接起来的值添加到之前创建的列表，  完成后计数器加1
            c1 = new_lie[-1]   
            c2 = df.loc[sy, '下单尺码']
            c3 = c1 + '/' + c2
            c4 = c3.split('/')
            c5 = set(c4)
            str1 = ''
            for k in c5:
                if len(str1) == 0:
                    str1 = k
                else:
                    str1 = str1 + '/' + k
            new_lie.append(str1)
            num += 1
df['现有尺码'] = new_lie
print(df)

