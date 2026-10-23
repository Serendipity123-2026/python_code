def count_char(s):
    zm_num = 0
    sz_num = 0
    ot_num = 0
    for i in s:
        if i.isalpha():
            zm_num += 1
        elif i.isdigit():
            sz_num += 1
        else:
            ot_num += 1
    return zm_num, sz_num, ot_num


zm, sz, ot = count_char("Hello Python 2026!")
print(f"字母：{zm}个，数字：{sz}个，其他：{ot}个")
