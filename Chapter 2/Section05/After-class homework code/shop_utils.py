__all__ = ["get_discount", "TOTAL"]

TOTAL = 500


def get_discount(price):
    return price * 0.8


def get_ship_fee(price):
    return 10 if price < 99 else 0
