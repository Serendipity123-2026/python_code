"""
定义一个函数 c_to_f，根据传入的摄氏温度，计算并返回对应的华氏温度。

公式：华氏温度 = 摄氏温度 × 9 / 5 + 32

要求：调用函数分别转换 0、37、100 摄氏度，并打印结果。

"""
print("-------- 温度转换器 --------")


def c_to_f(c: float) -> float:
    """
    将摄氏温度转为华氏温度
    :param c: 摄氏温度
    :return: 华氏温度
    公式：华氏温度 = 摄氏温度 × 9 / 5 + 32
    """
    f = (c * 9) / 5 + 32
    return round(f, 2)


temp_list = [0, 37, 100]
for temp in temp_list:
    result = c_to_f(temp)
    print(f"{temp}摄氏温度转华氏温度为{result}")
