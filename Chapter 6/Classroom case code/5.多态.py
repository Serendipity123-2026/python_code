# class Car:
#     def charge(self):
#         print('正在补充燃料...')
#
#     def start(self):
#         print('正在启动...')
#
#
# class FuelCar(Car):
#     def charge(self):
#         print('燃油汽车正在加油...')
#
#     def start(self):
#         print('燃油汽车正在启动...')
#
#
# class ElectricCar(Car):
#     def charge(self):
#         print('电动汽车正在充电...')
#
#     def start(self):
#         print('电动汽车正在启动...')
#
#
#
# def handle_charge(car: Car):       # 参数类型声明为父类 Car
#     car.charge()
#     car.start()
#
# def handle_start(car: Car):       # 参数类型声明为父类 Car
#     car.start()        # 燃油汽车正在启动...
#
#
# handle_charge(FuelCar())        # 燃油汽车正在加油...
# handle_charge(ElectricCar())    # 电动汽车正在充电...
#
# handle_start(FuelCar())        # 燃油汽车正在启动...
# handle_start(ElectricCar())    # 电动汽车正在启动...


class FuelCar:
    def charge(self):
        print('燃油汽车正在加油...')

    def start(self):
        print('燃油汽车正在启动...')


class ElectricCar:
    def charge(self):
        print('电动汽车正在充电...')

    def start(self):
        print('电动汽车正在启动...')


def handle_charge(duck):  # 参数类型声明为父类 Car
    duck.charge()
    duck.start()


handle_charge(FuelCar())  # 燃油汽车正在加油...
handle_charge(ElectricCar())  # 电动汽车正在充电...
