"""
    某图书借阅系统 DataFrame df 包含列：书名、类型、借阅次数、入库年份。请写出满足以下要求的代码：

    1. 筛选出"借阅次数 ≥ 30"且"类型为 小说 或 传记"的图书记录
    2. 将筛选结果先按"借阅次数"降序、再按"入库年份"升序排序，赋值给 df_top


"""

import pandas as pd

df = pd.read_csv("resources/book_borrow.csv")

df_result = df[(df['借阅次数'] >= 30) & (df['类型'].isin(['小说', '传记']))]
print(df_result)
df_top = df_result.sort_values(by=['借阅次数', '入库年份'], ascending=[False, True])
print(df_top)
