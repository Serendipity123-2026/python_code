"""
定义函数 apply_discount(price, func)，其中 func 是一个计算折扣价的函数，返回 func(price) 的结果。

再定义三个折扣函数：

- discount_9：打 9 折
- discount_8：打 8 折
- discount_half：打 5 折

要求：对原价 680 元的商品，分别调用 apply_discount 传入不同的折扣函数，打印三种折扣后的价格。

"""

print("-------- 任意个数求乘积 --------")


def apply_discount(price, func):
    """
    商品折扣计算
    :param price: 商品价格
    :param func: 折扣计算的函数
    :return: 打折后商品价格
    """
    return func(price)


def discount_9(price):
    return price * 0.9


def discount_8(price):
    return price * 0.8


def discount_half(price):
    return price * 0.5


price = 680
print(f"商品打9折的价格为：{apply_discount(price, discount_9)}")
print(f"商品打8折的价格为：{apply_discount(price, discount_8)}")
print(f"商品打5折的价格为：{apply_discount(price, discount_half)}")
