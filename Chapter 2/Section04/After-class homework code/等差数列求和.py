"""
定义递归函数 sum_n(n)，计算 1 + 2 + 3 + ... + n 的结果。

提示：f(n) = n + f(n-1)，当 n == 1 时返回 1。

要求：调用函数计算 n = 100 的结果并打印（预期结果 5050）。

"""

print("-------- 任意个数求乘积 --------")


def sum_n(n: int):
    """
    等差数列求和
    :param n: 等差数列
    :return:等差数列的和
    """
    if n == 1:
        return 1
    return n + sum_n(n-1)


print(sum_n(100))