"""
使用 random 模块实现猜数字游戏：

- 程序随机生成一个 1~100 的整数
- 用户循环输入猜测的数字
- 猜大了提示"猜大了，再小一点"，猜小了提示"猜小了，再大一点"
- 猜中后输出"恭喜你，猜对了！"并结束循环

"""

import random as rd

answer = rd.randint(0, 100)
# print(answer)
while True:
    num = int(input("请输入数字："))
    if num == answer:
        print("恭喜你，猜对了！")
        break
    elif num > answer:
        print("猜大了，再小一点")
    else:
        print("猜小了，再大一点")
