"""
定义两个函数：

- count_upper(s)：统计字符串中大写字母的个数
- analyze(s)：调用 count_upper，打印字符串及其中大写字母的个数

要求：调用 analyze("Python Is Fun And Easy")，预期输出大写字母个数为 5（P、I、F、A、E）。

"""

print("-------- 任意个数求乘积 --------")


def count_upper(s: str):
    """
    判断字符串中大写字母的个数
    :param s: 字符串
    :return: 大写字母的个数
    """
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count


def analyze(s: str):
    print(f"字符串：{s}")
    upper_num = count_upper(s)
    print(f"大写字母个数：{upper_num}")


analyze("Python Is Fun And Easy")

