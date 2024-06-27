# 《Pandas + Excel办公自动化》视频

#### 2024更新说明
本系列课程第一次更新于2020年，当时使用的版本为(pandas==1.1)，以下为一些 2024年 (python==3.12, pandas==2.2)的一些修正更新说明  

- A001, I001, I002
> 在 `pandas>=1.4.0` 版本, `pd.DataFrame.append` 已弃用, 请使用 `pd.concat`,  https://pandas.pydata.org/pandas-docs/version/1.5/whatsnew/v1.4.0.html#deprecated-dataframe-append-and-series-append

- B002
> `pd.read_excel()` date_parser 参数 于 `pandas>=2.0.0` 版本弃用, 
> 使用 `date_format` 代替，或者作为对象读入，然后根据需要应用 `to_datetime()`
``
- C002, F001, N012, N013
> `numpy.NaN` 于 2.0 版本弃用, 请使用 `np.nan` 代替

- D001
> `pd.Series` 对象使用 `[]` 按位置访问值如 `s[0]` 会报警告，请使用 `s.iloc[0]` 代替

- D003, L001
> 在 `pandas>=1.5.0` 版本, `groupby().sum()` `groupby().mean()` 等聚合操作, 聚合操作会保留非数值列。如果你希望只对数值列进行聚合，可以使用 `numeric_only=True` 参数

- G002
> 使用正则表达式时, '\d', '\s' 等字符会有 SyntaxWarning 警告，请在前面加 r 如 r'\d'，r'\s' 

- H006, N010, N020
> 在 `pandas>=2.2.0` 版本, dtypes 中的 offset(时间偏移) 的别名 H, BH, CBH, T, S, L, U, 和 N 被弃用, 请使用 h, bh, cbh, min, s, ms, us, and ns. https://pandas.pydata.org/docs/user_guide/timeseries.html#offset-aliases  
period(时间段) 别名 A, H, T, S, L, U, 和 N 被弃用, 请使用 Y, h, min, s, ms, us, and ns, https://pandas.pydata.org/docs/user_guide/timeseries.html#period-aliases  

| 旧别名 | 新别名 |
|-----|-----|
| A   | Y   |
| M   | ME  |
| H   | h   |
| BH  | bh  |
| CBH | cbh |
| T   | min |
| S   | s   |
| L   | ms  |
| U   | us  |
| N   | ns  |

- J002, K002
> 所有出现 `aggfunc=sum` 的地方, 改为 `aggfunc='sum'`

- N011
> `pd.Series.apply(convert_dtype=False)` 中的 `convert_dtype` 参数将被弃用, 
> 请使用 `pd.Series.astype(object).apply()` 代替

- N013
> FutureWarning: 以前的 `stack` 实现已弃用，并将在 `pandas` 的未来版本中删除。
> 有关详细信息，请参阅 `pandas==2.1.0` 的新注意事项。
> 指定 `future_stack=True` 以采用新的实现并禁止此警告。

- N021
> FutureWarning: `pct_change()` 除 `fill_method=None` 外，`fill_method` 的所有选项都已弃用。 
> 'limit' 参数已弃用，并将在未来的版本中删除。
> 要么在调用 `pct_change` 之前填充任何非前导 NA 值，要么指定 'fill_method=None' 来不填充 NA 值。

- O007
> `plt.style.use('seaborn-white')` 不可用, 请使用 `plt.style.use('seaborn-v0_8-white')` 替代
> 也可以打印 `plt.style.available` 查看可用的样式

- O013 
> `seaborn` 中 的多个方法的 ci 参数弃用, 使用 `errorbar=None` 或 `errorbar=('ci', False)` 代替  
> `seaborn.kdeplot(shade=True)` `shade` 参数将弃用, 使用 `fill=True` 代替
> `seaborn.distplot()` 已弃用, 请使用 `seaborn.histplot()` 代替

## 《Pandas + Excel办公自动化》网易云课堂地址(完整版):
https://study.163.com/course/introduction/1209966922.htm?share=2&shareId=480000002210461

##  BiliBili
Up主: AniPython
https://www.bilibili.com/cheese/play/ss24301
