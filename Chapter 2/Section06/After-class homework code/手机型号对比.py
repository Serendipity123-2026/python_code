"""
定义一个 Phone 类，包含品牌、型号、价格三个实例属性，
重写 __eq__ 魔法方法：当品牌、型号、价格都相同时返回 True。
创建两台 ("华为", "Mate 60", 5999) 的手机对象和一个 ("华为", "Mate 60", 6999) 的对象，
分别用 == 比较，输出比较结果

"""


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.price == other.price


phone1 = Phone("华为", "Mate 60", 5999)
phone2 = Phone("华为", "Mate 60", 5999)
phone3 = Phone("华为", "Mate 60", 6999)
print(phone1 == phone2)

print(phone1 == phone3)
