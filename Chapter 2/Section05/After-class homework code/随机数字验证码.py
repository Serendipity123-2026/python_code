"""
使用 random 模块，
生成一个 6 位数字验证码（每位数字为 0~9 的随机整数），
输出到屏幕。要求验证码的每一位通过 randint 生成，不能直接写死。
"""
import random as rd
code = ""
for i in range(6):
    code += str(rd.randint(0, 9))

print(code)