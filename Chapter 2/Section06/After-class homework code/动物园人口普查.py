class Animal:
    total = 0

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        # 每创建实例，类属性total +1
        Animal.total += 1


# 创建3个动物对象
a1 = Animal("小白", "狗")
a2 = Animal("花花", "猫")
a3 = Animal("大壮", "牛")

# 使用 类名.属性 打印总数
print(Animal.total)
