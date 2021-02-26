import pandas as pd
from glob import glob
import time
from multiprocessing import Pool, Manager

path1 = "/Users/Yi/Mirror/我的python教程/AskAndAnswer/multi_test_1/"
path2 = "/Users/Yi/Mirror/我的python教程/AskAndAnswer/multi_test_2/"


# 单进程
def concat_files(folder_path):
    afn_list = glob(folder_path + '*.xlsx')
    # print(afn_list)
    df_list = []

    for afn in afn_list:
        # t = time.time()
        df_temp = pd.read_excel(afn)
        # print('单进程读每个文件用时', time.time() - t)
        df_list.append(df_temp)

    df_all = pd.concat(df_list)
    print(df_all.shape)
    return df_all


def read_file(afn, df_list):
    # t = time.time()
    df = pd.read_excel(afn)
    # print('多进程读每个文件用时', time.time() - t)
    df_list.append(df)


# 多进程
def concat_files_multi(folder_path):
    afn_list = glob(folder_path + '*.xlsx')
    pool = Pool()
    df_list = Manager().list()
    # print('t1', round(time.time(), 2))
    for afn in afn_list:
        pool.apply_async(read_file, args=(afn, df_list))
    # print('t2', round(time.time(), 2))
    pool.close()
    # print('t3', round(time.time(), 2))
    pool.join()
    # print('t4', round(time.time(), 2))
    df_all = pd.concat(df_list)
    # print(df_all.shape)
    return df_all


if __name__ == '__main__':
    # t1 = time.time()
    # concat_files(path1)
    # t2 = time.time()
    # print("单进程用时", t2 - t1, '秒')
    # print('*' * 50)
    concat_files_multi(path2)
    # t3 = time.time()
    # print("多进程用时", t3 - t2, '秒')
