"""
定义一个 Rectangle 类，包含长、宽两个实例属性，
提供 area 方法计算面积、perimeter 方法计算周长。
创建长为8、宽为5的矩形对象，分别打印面积和周长

"""


class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rt = Rectangle(8, 5)
print(f"矩形的面积为：{rt.area()}")
print(f"矩形的周长为：{rt.perimeter()}")
