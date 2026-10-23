def is_phone(s):
    """
    判断手机号是否为 11位
    :param s: 手机号
    :return: 是或否
    """
    if len(s) == 11:
        return True
    else:
        return False
