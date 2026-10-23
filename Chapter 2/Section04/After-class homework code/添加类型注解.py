"""
为下面的函数添加完整的类型注解（参数和返回值），并用一句话说明类型注解的作用。

    def bmi(weight, height):
        return round(weight / (height ** 2), 1)

要求：注解后调用 bmi(70, 1.75)，输出结果为 22.9。

"""

print("-------- 添加类型注解 --------")


def bmi(weight, height):
    """
    计算身高体重指数BMI
    :param weight:体重
    :param height:身高
    :return:高体重指数BMI(结果保留1位小数)
    """

    return round(weight / (height ** 2), 1)


print(bmi(70, 1.75))