"""
Python Pandas Excel 学习群: 366719470
Ask And Answer 问答
AAA007 使用 多进程 同时读取多个文件
"""
import pandas as pd
from glob import glob
from multiprocessing import Manager, Pool
import time


path1 = "/Users/Yi/Mirror/我的python教程/AskAndAnswer/multi_test_1/"
path2 = "/Users/Yi/Mirror/我的python教程/AskAndAnswer/multi_test_2/"
path3 = "/Users/Yi/Downloads/aaa/"


# 单进程
def concat_files(folder_path):
    afn_list = glob(folder_path + '*.xlsx')

    df_list = []
    for afn in afn_list:
        df_temp = pd.read_excel(afn)
        df_list.append(df_temp)

    df_all = pd.concat(df_list)
    print(df_all.shape)
    return df_all


def read_file(afn, df_list):
    df = pd.read_excel(afn)
    df_list.append(df)


# 多进程
def concat_files_multi(folder_path):
    afn_list = glob(folder_path + '*.xlsx')
    # print(afn_list)
    print('t1: ', round(time.time(), 2))
    df_list = Manager().list()
    pool = Pool(2)
    print('t2: ', round(time.time(), 2))
    for afn in afn_list:
        pool.apply_async(
            read_file,
            args=(afn, df_list)
        )
    print('t3: ', round(time.time(), 2))
    pool.close()
    print('t4: ', round(time.time(), 2))
    pool.join()  # 8 秒
    print('t5: ', round(time.time(), 2))

    df_all = pd.concat(df_list)
    print(df_all.shape)
    return df_all


if __name__ == '__main__':
    # t1 = time.time()
    # concat_files(path2)
    # t2 = time.time()
    # print('单进程用时: ', t2 - t1, '秒')
    df = concat_files_multi(path3)
    print(df.head())
    # t3 = time.time()
    # print('多进程用时: ', t3 - t2, '秒')
