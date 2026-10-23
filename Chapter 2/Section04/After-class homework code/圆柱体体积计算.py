"""
定义一个函数 cylinder_volume，根据传入的底面半径 r 和高 h，计算圆柱体的体积（π 取 3.14，结果保留 2 位小数）。

要求：

1. 为函数编写完整的说明文档（Docstring），包含 :param 和 :return 说明
2. 调用函数计算半径为 5、高为 10 的圆柱体积并打印

"""
print("-------- 圆柱体体积计算 --------")


def cylinder_volume(r: float, h: float) -> float:
    """
    计算圆柱体的体积
    :param r: 圆柱体的底面半径
    :param h: 圆柱体的高
    :return: 圆柱体的体积
    V = π * r ** 2 * h
    """
    return round(3.14 * r ** 2 * h)


radius = float(input("请输入圆柱体的底面半径："))
high = float(input("请输入圆柱体的高："))
volume = cylinder_volume(radius, high)
print(f"底面半径为{radius}  高为{high}的圆柱体的体积为{volume}")
