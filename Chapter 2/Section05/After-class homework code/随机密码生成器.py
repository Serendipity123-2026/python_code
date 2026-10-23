# import random as rd
# import string
#
# password = ""
# for i in range(8):
#     s = rd.choice(string.ascii_lowercase)
#     num = str(rd.randint(0, 9))
#     password += rd.choice([s, num])
# print(password)

from random import choice

# 定义字符池：小写字母 + 数字
letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
pool = letters + digits

pwd = ""
# 循环8次，每次随机选1个字符
for _ in range(8):
    pwd += choice(pool)

print(pwd)
