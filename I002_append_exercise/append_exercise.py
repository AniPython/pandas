"""
使用 append() 函数
合并一个文件夹里面的全部表格
"""
import os
import pandas as pd


def v_concat_files(folder: str) -> pd.DataFrame:
    df_all = pd.DataFrame()
    for fn in os.listdir(folder):
        ffn = os.path.join(folder, fn)
        print(ffn)
        df_temp = pd.read_excel(ffn)
        df_all = df_all.append(df_temp)  # 报错
    return df_all


if __name__ == '__main__':
    # df_A = v_concat_files(
    #     '/Users/Yi/Mirror/我的python教程/Pandas办公自动化/z_data_source/PlatformA'
    # )
    # df_A.info()
    # print(df_A.head())
    # df_A.to_excel('all_A.xlsx')
    # df_A['平台'] = '平台A'
    #
    # with pd.ExcelWriter(
    #     'all_A.xlsx',
    #     datetime_format='YYYY-MM-DD'
    # ) as writer:
    #     df_A.to_excel(writer, index=False)

    df_B = v_concat_files(
        '../z_data_source/PlatformB'
    )
    df_B['平台'] = '平台B'
    with pd.ExcelWriter(
        'all_B.xlsx',
        datetime_format='YYYY-MM-DD'
    ) as writer:
        df_B.to_excel(writer, index=False)
