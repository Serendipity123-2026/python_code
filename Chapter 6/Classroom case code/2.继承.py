class Car:
    brand = ""
    name = ""
    price = ""
    color = ""

    def start(self):
        print("汽车启动")

    def run(self):
        print("汽车运行")

    def stop(self):
        print("汽车停止")

class Ele_Car(Car):
    ele = ""

    def add_ele(self):
        print("添加电能")


class Oil_Car(Car):
    oil = ""

    def add_oil(self):
        print("添加汽油")


if __name__ == '__main__':
    ele_car = Ele_Car()
    ele_car.start()
