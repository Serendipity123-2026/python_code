"""
定义函数 make_member_card(name, **kwargs)，用于生成会员卡信息：

- name 为会员姓名
- kwargs 接收任意个配置项，如：months=12（时长）、coach=True（私教）、locker=True（储物柜）

要求：

1. 在函数内打印会员姓名和所有配置项
2. 调用时传入不同数量的配置项，观察 kwargs 的内容变化

"""

print("-------- 健身房会员卡定制 --------")


def make_number_card(name, **kwargs):
    """
    输出会员名字和对应信息
    :param name:会员名字
    :param kwargs:会员的其他信息
    """

    print(f"会员的名字为：{name}")
    print(f"会员的配置为：{kwargs}")
    for k,v in kwargs.items():
        print(f"{k} ：{v}")


make_number_card("lisi",months=12,coach=True)
make_number_card("ww",months=12,coach=True,locker=True)