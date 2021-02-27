from datetime import date

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from generic.ufunc import insert_img_to_excel
from tasks.unify_tables import unify_tb
from tasks.unify_tables import unify_jd


# 1) 下载数据源
def download_data_source():
    print('下载数据源')


# 2) 输出销售总表
def out_all_sales():
    # 1.合并全部销售表格
    df_jd = unify_jd()
    df_tb = unify_tb()

    df = pd.concat([df_jd, df_tb], ignore_index=True)

    # 2.读取表格
    df_goods_base = pd.read_excel('./data_source/goods_base.xlsx')

    df_cost_other = pd.read_excel('./data_source/cost_other.xlsx')

    df_cost_platform = pd.read_excel('./data_source/cost_platform.xlsx')
    df_cost_platform = df_cost_platform[df_cost_platform['备注'] == '常规']
    df_cost_platform = df_cost_platform[['平台', '扣点']]

    # 3. 连接
    df = pd.merge(df, df_goods_base, on='货号', how='left', validate='m:1')
    df = pd.merge(df, df_cost_other, on='季节', how='left', validate='m:1')
    df = pd.merge(df, df_cost_platform, on='平台', how='left', validate='m:1')

    # 4. 计算
    df.loc[
        (df['平台'] == '京东') &
        (df['日期'].dt.date >= date(2020, 6, 10)) &
        (df['日期'].dt.date <= date(2020, 6, 20)),
        '扣点'
    ] = 0.12

    df.loc[
        df['退货'] == 0,
        '退货金额'
    ] = 0

    df['收入'] = df['实收金额'] * df['销量'] - df['退货金额'] * df['退货']

    # 扣平台费用
    df['利润'] = df['收入'] * (1 - df['扣点'])
    # 扣物料成本
    df['利润'] = df['利润'] - df['成本'] * df['销量']
    # 扣其它费用
    df['利润'] = df['利润'] - (df['销量'] + df['退货']) * (df['上架费'] + df['包装费'] + df['物流费'])

    df.to_excel('./data_out/all_sales.xlsx', index=False)

    df.to_pickle('./data_out/all_sales.pkl')


# 3) 输出统计数据
def out_statistics_1():
    # df = pd.read_excel('/Users/Yi/Mirror/我的python教程/Sales/data_out/all_sales.xlsx')
    df = pd.read_pickle('./Sales/data_out/all_sales.pkl')

    df = pd.pivot_table(
        df,
        index='货号',
        values=['实收金额', '销量', '收入', '利润'],
        aggfunc=sum
    ).reset_index()

    df = df.reindex(columns=['货号', '图片', '实收金额', '销量', '收入', '利润'])

    afn = './data_out/goods_id_statistics.xlsx'
    df.to_excel(afn, index=False)

    insert_img_to_excel(
        filename=afn,
        by_col='A',
        to_col='B',
        img_folder='./data_source/goods_image'
    )


# 4) 输出统计数据
def out_statistics_2():
    df = pd.read_pickle('./data_out/all_sales.pkl')

    sns.set()
    plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB']  # mac
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # win
    plt.rcParams['axes.unicode_minus'] = False

    df['月份'] = df['日期'].dt.month

    sns.barplot(x='月份', y='销量', hue='平台',
                data=df, estimator=sum, ci=None)

    plt.savefig('./data_out/月份_销量.png', dpi=150)


if __name__ == '__main__':
    # out_all_sales()
    # out_statistics_1()
    out_statistics_2()

    # import time
    # t1 = time.time()
    # df1 = pd.read_excel('/Users/Yi/Mirror/我的python教程/Sales/data_out/all_sales.xlsx')
    #
    # t2 = time.time()
    # df2 = pd.read_pickle('/Users/Yi/Mirror/我的python教程/Sales/data_out/all_sales.pkl')
    # t3 = time.time()
    #
    # print(t2 - t1)
    # print(t3 - t2)

