"""
定义一个 Pet 类，包含名字、年龄、种类三个实例属性（在 __init__ 中定义），
并提供一个实例方法 introduce，输出格式为：
我是小柯基，今年2岁，是一只狗狗。
创建一个名字为"小柯基"、年龄为2、种类为"狗狗"的对象并调用方法

"""


class Pet:
    def __init__(self, name: str, age: int, kind: str):
        self.name = name
        self.age = age
        self.kind = kind

    def introduce(self):
        print(f"我是{self.name}，今年{self.age}岁，是一只{self.kind}")


pet = Pet("小柯基", 2, "狗狗")
pet.introduce()