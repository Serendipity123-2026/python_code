# num = int(input("请输入数字："))
# if num % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")
#
#
#
# age = int(input("请输入年龄："))
# if age >= 18:
#     print("成年")
#
# else:
#     print("未成年")
#
# num = int(input("请输入数字："))
# if num > 0:
#     print("正数")
# else:
#     print("负数")
#
# score = int(input("请输入成绩："))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")


# score = int(input("请输入成绩："))
# if score >= 85:
#      print("优秀")
# elif score >= 60:
#      print("及格")
# else:
#      print("不及格 ")


# total = int(input("请输入商品总额："))
# price = 0
# if total >= 500:
#     price = total * 0.8
# elif total >= 300:
#     price = total * 0.9
# elif total >= 100:
#     price = total * 0.95
# else:
#     price = total
# print("实际应付金额：", price)

# a = int(input("请输入三角形第一条边为："))
# b = int(input("请输入三角形第二条边为："))
# c = int(input("请输入三角形第三条边为："))
#
# if a + b > c or a + c > b or b + c > a:
#     if a == b == c:
#         print("等边三角形")
#     elif a == b or a == c or b == c:
#         print("等腰三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不是三角形")

# ele = float(input("请输入用电度数："))
# price = 0.0
# if ele < 2880:
#     price = ele * 0.4883
# elif ele < 4800:
#     price = (2880 * 0.4883) + (ele - 2880) * 0.5383
# else:
#     price = (2880 * 0.4883) + ((4800 - 2880) * 0.5383) + (ele - 4800) * 0.7883
# print("电费为：", price)


# num1 = float(input("请输入第一个数"))
# num2 = float(input("请输入第二个数"))
# opt = input("请输入符号：")
#
# match opt:
#     case "+":
#         print(f"{num1} {opt} {num2} = {num1+num2}")
#     case "-":
#         print(f"{num1} {opt} {num2} = {num1-num2}")
#     case "*":
#         print(f"{num1} {opt} {num2} = {num1*num2}")
#     case "/":
#         print(f"{num1} {opt} {num2} = {num1/num2}")
#     case _:
#         print("输入错误")


# command = input("请输入指令：")
# match command:
#     case "上" | "W" | "w":
#         print("角色向上移动")
#     case "下" | "S" | "s":
#         print("角色向下移动")
#     case "左" | "A" | "a":
#         print("角色向左移动")
#     case "右" | "D" | "d":
#         print("角色向右移动")
#     case "跳" | " ":
#         print("角色跳跃")
#     case "攻击" | "J" | "j":
#         print("角色发动攻击")
#     case "退出" | "ESC" | "esc":
#         print("角色退出游戏")
#     case _:
#         print("未知指令")
#
# i = 0
# while i < 10:
#     print("人生苦短，我用Python~")
#     i += 1
#
# i = 1
# sum = 0
# while i < 101:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)
#
# string = "Hello-Python"
# for i in string:
#     print(i)
#
# print("======================================================")
#
# sum = 0
# for i in range(1, 101, 2):
#     sum += i
# print(f"1-100 之间所有的奇数之和为：{sum}")
#
# sum = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         sum += i
# print(f"1-100 之间所有的奇数之和为：{sum}")
#
# print("======================================================")
# sum = 0
# for i in range(100, 501, 3):
#     sum += i
# print(f"100-500 之间所有3的倍数之和为：{sum}")
#
# sum = 0
# for i in range(100, 501):
#     if i % 3 == 0:
#         sum += i
# print(f"100-500 之间所有3的倍数之和为：{sum}")


# for hour in range(24):
#     for minute in range(60):
#         print("%02d:%02d" % (hour, minute))



