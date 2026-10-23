def c_to_f(c):
    """
    摄氏温度转华氏温度
    :param c: 摄氏温度
    :return: 华氏温度
    """
    f = c * 9 / 5 + 32
    return round(f, 1)


def f_to_c(f):
    """
    华氏温度转摄氏温度
    :param f: 华氏温度
    :return: 摄氏温度
    """
    c = (f - 32) * 5 / 9
    return round(c, 1)


MALE_BMI_MAX = 24.9
FEMALE_BMI_MAX = 23.9


def bmi(weight, height):
    return weight / height ** 2