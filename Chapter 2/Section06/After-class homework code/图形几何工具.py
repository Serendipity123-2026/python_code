class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

    def perimeter(self):
        return 2 * self.PI * self.radius


circle = Circle(5)
print(f"圆的面积是{round(circle.area(), 2)}")
print(f"圆的周长是{round(circle.perimeter(), 2)}")
