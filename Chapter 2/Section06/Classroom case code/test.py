# class Car:
#     pass
#
#
# car = Car()
# car.color = "red"
# car.brand = "tsl"
# car.price = 100000
# car.speed = 200
# car.start = lambda: print("汽车启动")
# car.stop = lambda: print("汽车停止")
# print(car.__dict__)
#
# car.start()
# car.stop()

# class Pet:
#     def __init__(self, name, age, kind):
#         self.name = name
#         self.age = age
#         self.kind = kind
#
#     def introduce(self):
#         print(f"我是{self.name}，今年{self.age}岁，是一只{self.kind}")
#
#
# pet = Pet("小柯基", 2, "狗狗")
# pet.introduce()

nums = [0, 0, 1, 0, 2, 0, 3]
for n in nums:
    if n == 0:
        nums.remove(n)
print(nums)