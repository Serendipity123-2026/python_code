"""
使用 import math 导入数学模块，
编写程序：输入圆柱的底面半径和高，
输出圆柱体积，结果保留 2 位小数。
"""
import math


def cylinder_volume(base_radius: float, height: float):
    """
    求圆柱体的体积
    :param base_radius: 圆柱体的底面半径
    :param height: 圆柱体的高
    :return: 圆柱体的体积
    """
    return round(math.pi * base_radius ** 2 * height, 2)


r = float(input("请输入圆柱底面半径: "))
h = float(input("请输入圆柱的高: "))
print(f"圆柱体的体积为：{cylinder_volume(r, h)}")

