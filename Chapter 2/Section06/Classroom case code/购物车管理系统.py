class Goods:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"商品名称：{self.name}， 商品价格：{self.price}, 商品数量：{self.quantity}"


class ShoppingCart:
    def __init__(self):
        self.goods_dict = {}

    @staticmethod
    def _is_int_input(prompt):
        while True:
            try:
                res = int(input(prompt))
                return res
            except ValueError:
                print("输入不是数字，请重新输入！")

    def add_goods(self):
        name = input("请输入商品名称：")
        if name in self.goods_dict:
            print("该商品已存在")
            return
        price = self._is_int_input("请输入商品价格：")
        quantity = self._is_int_input("请输入商品数量：")
        self.goods_dict[name] = Goods(name, price, quantity)
        print("商品添加成功")

    def mod_goods(self):
        name = input("请输入要修改的商品名称：")
        if name not in self.goods_dict:
            print("该商品不存在")
            return
        mod_price = self._is_int_input("请输入商品价格：")
        mod_quantity = self._is_int_input("请输入商品数量：")
        self.goods_dict[name] = Goods(name, mod_price, mod_quantity)
        print("商品修改成功")

    def del_goods(self):
        name = input("请输入要删除的商品名称：")
        if name not in self.goods_dict:
            print("该商品不存在")
            return
        del self.goods_dict[name]
        print("商品删除成功")

    def show_goods(self):
        for goods in self.goods_dict.values():
            print(goods)

    def run(self):
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("# 1.添加购物车   2.修改购物车   3.删除购物车   4.查询购物车   5.退出系统  #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print()

            choice = int(input("请输入你的选择："))

            match choice:
                case 1:
                    self.add_goods()
                case 2:
                    self.mod_goods()
                case 3:
                    self.del_goods()
                case 4:
                    self.show_goods()
                case 5:
                    print("退出系统")
                    break
                case _:
                    print("输入错误，请重新输入")


if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.run()