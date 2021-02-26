import pandas as pd
from glob import glob
from multiprocessing import Manager, Pool
import time

# path1 = r"E:/PY示例/aaa/"
path1 = "/Users/Yi/Downloads/aaa/"


# 单进程
def concat_files(folder_path):
    afn_list = glob(folder_path + '*.xlsx')
    df_list = []
    for afn in afn_list:
        df_temp = pd.read_excel(afn)
        df_list.append(df_temp)
    print(df_list)
    df_all = pd.concat(df_list)
    print(df_all.shape)


# 多进程

def read_file(afn, df_list):
    df = pd.read_ecxel(afn)
    print(df)
    df_list.append(df)


def concat_files_multi(folder_path):
    afn_list = glob(folder_path + '*.xlsx')
    print(afn_list)
    df_list = Manager().list()
    pool = Pool()
    for afn in afn_list:
        pool.apply_async(
            read_file,
            args=(afn, df_list)
        )
    pool.close()
    pool.join()  # 8 秒
    print(df_list)
    df_all = pd.concat(df_list)
    print(df_all.shape)
    return df_all


if __name__ == '__main__':
    # t1 = time.time()
    # concat_files(path1)
    # t2 = time.time()
    # print('单进程用时: ', t2 - t1, '秒')
    concat_files_multi(path1)
    # t3 = time.time()
    # print('多进程用时: ', t3 - t2, '秒')
