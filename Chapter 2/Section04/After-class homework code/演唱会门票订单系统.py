"""
定义函数 calc_ticket_total(*tickets, member_discount=1.0, delivery=0)，计算一笔门票订单的总金额：

- tickets：不定长参数，每张门票用元组表示 ("票档名称", 单价, 数量)
- member_discount：默认参数ji，会员折扣系数（默认 1.0 不打折，VIP 传 0.88）
- delivery：默认参数，快递费（默认 0，邮寄实体票传 15）

计算规则：

1. 先计算所有门票的小计之和（单价 × 数量）
2. 再乘以会员折扣系数
3. 最后加上快递费

要求：

1. 普通观众购买内场票 2 张（每张 1280）、看台票 3 张（每张 380），不邮寄，计算总价
2. VIP 会员（折扣 0.88）购买内场票 1 张（1280）、看台票 2 张（380），需邮寄（15 元），计算总价

"""

print("-------- 演唱会门票订单系统 --------")


def calc_ticket_total(*tickets, member_discount=1.0, delivery=0):
    sum_price = 0
    for name, price, num in tickets:
        sum_price += price * num
    total = sum_price * member_discount + delivery
    return total


print(f"普通观众：{calc_ticket_total(("内场票", 1280, 2), ("内场票", 380, 3))}")
print(f"VIP观众：{calc_ticket_total(("内场票", 1280, 1), ("内场票", 380, 2), member_discount=0.88, delivery=15)}")
