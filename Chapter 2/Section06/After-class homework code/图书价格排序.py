"""
定义一个 Book 类，包含书名和价格两个实例属性，
重写 __lt__ 魔法方法（按价格比较）。
创建三本书：("三体", 45)、("活着", 28)、("百年孤独", 39.5)，
将它们放入列表并用 sort() 排序后，按顺序打印书名（从便宜到贵）

"""


class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


book1 = Book("三体", 45)
book2 = Book("活着", 28)
book3 = Book("百年孤独", 39.5)
