import matplotlib.pyplot as plt
import os

def ax1_drow_fun():
    # 绘制子图 ax1(柱状图)
    countries = ['美国', '中国', '英国', '德国', '法国', '俄罗斯', '韩国', '印度', '沙特阿拉伯', '伊拉克', '伊朗']
    oil_reserves = [32, 35, 7, 12, 15, 71, 9, 12, 88, 71, 65]
    # 绘制柱状图
    ax1.bar(countries, oil_reserves, color='green')
    # 设置柱状图的标题
    ax1.set_title('世界各国石油储备', fontsize=18, fontweight='bold', pad=10)
    # 设置 x轴
    ax1.set_xlabel('国家', fontsize=14)
    # 设置 y轴
    ax1.set_ylabel('石油储备(亿吨)', fontsize=14)
    ax1.set_yticks([i for i in range(0, 110, 10)])
    # 设置网格
    ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.4)


def ax2_drow_fun():
    # 子图2(饼状图)
    countries2 = ['印度', '中国', '美国', '印尼', '巴基斯坦', '尼日利亚', '巴西', '俄罗斯', '其他']
    values = [14.51, 14.09, 3.4, 2.83, 2.51, 2.33, 2.12, 1.44, 20]
    ax2.pie(values, labels=countries2, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
    # 设置饼状图的标题
    ax2.set_title('世界各国人口比例', fontsize=18, fontweight='bold')
    # 设置图例
    ax2.legend(title='国家', loc='lower center', ncols=5, bbox_to_anchor=(0.5, -0.09))


def main():
    global ax1, ax2
    if not os.path.exists("./resources"):
        os.makedirs("./resources")

    # 图表支持中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 创建子图  nrows: 行数，ncols: 列数 , figsize: 图像大小 , dpi: 图像分辨率
    figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)
    # 获取子图对象
    ax1 = axes[0]
    ax2 = axes[1]
    ax1_drow_fun()
    ax2_drow_fun()

    plt.savefig("./resources/photo.png")

    plt.show()


if __name__ == '__main__':
    main()

