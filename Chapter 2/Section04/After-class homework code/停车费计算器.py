"""
某停车场收费规则如下：

- 半小时以内（含）免费
- 超过半小时、1小时以内（含），收费 10 元
- 超过1小时后，每小时加收 5 元（不足1小时按1小时算）

定义函数 parking_fee(hours, base=10, extra=5)，其中 base（首小时费用）和 extra（后续每小时费用）为默认参数，返回应缴纳的停车费。

要求：

1. 不传 base、extra，计算停车 2.5 小时的费用
2. VIP 车主首小时费用为 5 元、后续每小时 2 元，用关键字参数计算停车 3 小时的费用

"""
import math

print("-------- 停车费计算器（默认参数） --------")


def parking_fee(hours: float, base: int = 10, extra: int = 5):
    """
    停车费计算
    :param hours: 停车时间
    :param base:  首小时的费用
    :param extra: 后续每小时的费用
    :return: 停车总费用
    """
    if hours <= 0.5:
        print("停车时长未超过半小时不收费")
        return 0
    elif hours <= 1:
        return base
    else:
        over = hours - 1
        over = math.ceil(over)
        return base + over * extra


print(f"普通车主停车费用为{parking_fee(2.5)}元")
print(f"VIP车主停车费用为{parking_fee(5, extra=2)}元")