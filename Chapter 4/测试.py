import csv
import os.path

text = """
    【跑腿订单】PT20260415 已完成，接单员 13900001234，跑腿费 ￥6.50，下单 2026-04-15；
    【跑腿订单】PT20260417 进行中，接单员 15877779999，跑腿费 ￥12.00，下单 2026-04-17；
    【跑腿订单】PT20260418 已取消，接单员 18600002222，跑腿费 ￥9.50，下单 2026-04-18；
    客服邮箱 runner@example.com，客服座机 027-88886666。
"""

def clean_orders(text):
    if not os.path.exists("/data/order_messages"):
        os.makedirs("/data/order_messages.csv")

    with open("/data/order_messages.csv", "w", encoding="utf-8", newline="") as f:
        write = csv.DictWriter(f, fieldnames=["【跑腿订单】", "订单状态", "接单员", "跑腿费", "下单时间", "客服邮箱",
                                              "客服座机"])

        write.writeheader()

if __name__ == '__main__':
    clean_orders(text)
