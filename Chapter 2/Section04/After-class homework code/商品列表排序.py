"""
有如下商品数据：

    goods = [
        {"name": "耳机", "price": 199},
        {"name": "手机", "price": 4999},
        {"name": "手机壳", "price": 29},
        {"name": "充电宝", "price": 89},
    ]

要求：
1. 使用 lambda 配合 sort，按价格从低到高排序并打印
2. 使用 lambda 配合 sort，按价格从高到低排序并打印（提示：reverse=True）

"""

print("-------- 任意个数求乘积 --------")

goods = [
    {"name": "耳机", "price": 199},
    {"name": "手机", "price": 4999},
    {"name": "手机壳", "price": 29},
    {"name": "充电宝", "price": 89},
]

goods.sort(key=lambda goods: goods["price"])
print(f"价格从低到高排序为：{goods}")
goods.sort(key=lambda goods: goods["price"], reverse=True)
print(f"价格从高到低排序为：{goods}")