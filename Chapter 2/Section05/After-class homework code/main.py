# 11. __name__ 的应用
from greet import greet

greet("小明")

# 12. __all__ 控制导入范围
from shop_utils import *
print(TOTAL)
print(get_discount(100))
# print(get_ship_fee(50))


# 13. 包的应用（helpers 包）
import helpers.str_util
import helpers.num_util

print(helpers.str_util.is_phone("13800138000"))
print(helpers.num_util.PI)


from helpers import str_util, num_util

print(str_util.is_phone("13800138000"))
print(num_util.PI)


from helpers.str_util import is_phone
from helpers.num_util import PI

print(is_phone("13800138000"))
print(PI)

