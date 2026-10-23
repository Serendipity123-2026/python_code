# # 这是单行注释 （快捷键 Ctrl + /）
# print("Hello World!")
# print("Hello Python!")
#
# """
# 这是多行注释
# print函数结尾默认加\n  可以通过 end= 来改变
# """
# print("Hello World!", end="#")
# print("Hello Python!")

import re

s = "订单号 PT20260415，金额 ￥6.50，另有 PT2026041 与 PT202604157"
print(len(re.findall(r"PT\d{8}", s)))