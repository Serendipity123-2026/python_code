class Car:
    def __init__(self, brand, name, price, speed):
        self.brand = brand
        self.name = name
        self.price = price
        self.__speed = speed

    # 获取速度
    def get_speed(self):
        return self.__speed

    # 设置速度
    def set_speed(self, speed):
        if speed < 0:
            print("速度不能为负数")
            return
        self.__speed = speed

    # 启动
    def start(self):
        print(f"汽车启动,速度的为：{self.__speed}")

    # 停止
    def stop(self):
        print("汽车停止")

    def __speed_up(self):
        print(f"汽车加速,速度为：{self.__speed}")


if __name__ == '__main__':
    car = Car("奔驰", "GLC", 300000, 200)

    car.set_speed(180)
    car.start()
    car.stop()
