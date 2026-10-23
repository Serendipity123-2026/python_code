class Goods:
    next_id = 1001

    def __init__(self, name, price, stock):
        self.id = Goods.next_id
        Goods.next_id += 1
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"[{self.id}] {self.name} | 单价：{self.price}元 | 库存：{self.stock}件"


class MallSystem:
    def __init__(self):
        self.goods_list = []
        self.goods_list.append(Goods("机械键盘", 299, 100))
        self.goods_list.append(Goods("无线鼠标", 129, 200))
        self.goods_list.append(Goods("显示器", 1099, 30))

    @staticmethod
    def is_int_input(v: int):
        while True:
            try:
                res = int(input(v))
                return res
            except ValueError:
                print("输入的不是数字，请重新输入！")

    @staticmethod
    def is_float_input(v: float):
        while True:
            try:
                res = float(input(v))
                return res
            except ValueError:
                print("输入的数字不规范，请重新输入！")

    def add_goods(self):
        name = input("请输入要添加的商品名称：")
        for g in self.goods_list:
            if g.name == name:
                print("该商品已存在")
                return
        price = self.is_float_input("请输入商品价格：")
        stock = self.is_int_input("请输入商品数量：")
        self.goods_list.append(name, price, stock)
        print("商品添加成功")

    def select_goods(self):
        for v in self.goods_list:
            print(v)

    def mod_goods(self):
        name = input("请输入要修改的商品名称：")
        for g in self.goods_list:
            if g.name == name:
                print("该商品已存在")
                return
        price = self.is_float_input("请输入商品价格：")
        stock = self.is_int_input("请输入商品数量：")
        self.goods_list.append(name, price, stock)
        print("商品添加成功")

    def del_goods(self):
        pass

    def show_goods(self):
        pass

    def count_goods(self):
        pass

    def run(self):
        while True:
            print("==============================================")
            print("1.添加商品\t2.查询商品\t3.修改商品\n4.删除商品\t5.展示全部\t6.库存统计\t7.退出系统")
            print("==============================================")
            print()
            choice = int(input("请输入值"))

            match choice:
                case 1:
                    self.add_goods()
                case 2:
                    self.select_goods()


if __name__ == '__main__':
    ms = MallSystem()
    ms.run()
