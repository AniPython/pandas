import pandas as pd
from time import time


def use_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        use = round(time() - start, 3)
        print('%s()用时: %s秒' % (func.__name__, use))
        return result

    return wrapper


@use_time
def read_excel(fn):
    df = pd.read_excel(fn)
    return df


@use_time
def read_pickle(fn):
    df = pd.read_pickle(fn)
    return df


@use_time
def write_pickle(df):
    df.to_pickle('2019.pkl')


if __name__ == '__main__':
    df1 = read_excel('2019.xlsx')
    df1.info()
    print('*' * 30)
    df2 = read_pickle('2019.pkl')
    df2.info()
    # write_pickle(df)
