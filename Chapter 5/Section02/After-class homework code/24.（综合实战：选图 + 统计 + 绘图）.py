"""
    某图书馆管理系统 DataFrame df 包含列：借出日期、书库（文学库/科技库/少儿库/综合库）、借出数量。

    请编写代码完成：

    1. 配置运行环境：导入 pandas 和 matplotlib、解决中文显示
    2. 创建 1 行 2 列的子图画布
    3. 统计每个书库的总借出数量，在左侧子图绘制柱状图（提示：df.groupby('书库')['借出数量'].sum()）
    4. 统计每个书库的订单数占比（即每个书库出现了多少条借出记录），在右侧子图绘制饼状图，显示百分比和标签
    5. 两个子图分别设置标题，最后将画布保存为 library_stats.png 并显示

"""

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']

figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

figure.suptitle('图书馆借出统计', fontsize=20)

ax1 = axes[0]
ax2 = axes[1]
# 读取数据
df = pd.read_csv("./resources/library_borrow.csv", encoding='utf-8')
# 获取数据
borrow_num = df.groupby('书库')['借出数量'].sum()
x = borrow_num.index
y = borrow_num.values

# 绘制柱状图
ax1.bar(x, y, width=0.3)

ax1.set_title('每个书库的总借出数量')

ax1.set_xlabel("书库", fontsize=14)
ax1.set_ylabel("总借出数量", fontsize=14)

ax2.pie(y, labels=x, autopct='%1.1f%%')

ax2.set_title('每个书库的订单数占比')

ax2.legend(loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.07))

figure.savefig('./resources/library_stats.png')


plt.show()
