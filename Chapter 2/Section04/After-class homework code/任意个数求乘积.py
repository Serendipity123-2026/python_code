"""
定义函数 product，接收任意个数的数字参数，计算并返回它们的连乘结果。

要求：

1. 调用 product(2, 3, 4)，输出 24
2. 调用 product(5, 10, 2, 8)，输出 800
3. 在函数内打印 args 的类型，验证它是元组

"""

print("-------- 任意个数求乘积 --------")


def product(*args):
    """
    求元组每个元素相乘的乘积
    :param args:元组
    :return:元组每个元素相乘的乘积
    """
    result = 1
    for i in args:
        result *= i
    print(type(args))
    return result


print(product(2, 3, 4))
print(product(5, 10, 2, 8))