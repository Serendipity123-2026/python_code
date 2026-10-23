print("-------- 题目1 --------")
num = 1114.1
print(num)
num += 1
print(num)
num = "OK"
print(num)

print("-------- 题目2 --------")
a = 10
b = "Python"
c = 3.14
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("-------- 题目3 --------")
a = 10
b = 20
a, b = b, a
print(a, b)

print("-------- 题目4 --------")
print("床前明月光\n疑是地上霜")

print("-------- 题目5 --------")
name = "小明"
age = 12
pro = "软件工程"
print(f"大家好，我是{name}，今年{age}岁，学习的专业是{pro}")

print("-------- 题目6 --------")
name = input("您的姓名是：")
age = input("您的年龄为：")
print(f"您输入的姓名是：{name}\n您输入的年龄为：{age}")

print("-------- 题目7 --------")
num1 = int(input("请输入整数1："))
num2 = int(input("请输入整数2："))
print(f"{num1}+{num2}={num1 + num2}")

print("-------- 题目8 --------")
balance = 10000
take = float(input("请输入取款金额："))
balance -= take
print("取款后您的银行卡余额为：", balance)

print("-------- 题目9 --------")
# num_str = "3.14"
# num = float(num_str) + 1
# print(num)
num_str = "3.14"
num = float(num_str)
result = num + 1
print(f"{result:.2f}")

print("-------- 题目10 --------")
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
num3 = int(input("请输入第三个整数："))
avg = (num1 + num2 + num3) / 3
print("平均数为：", avg)

print("-------- 题目11 --------")
Upper_sole = float(input("请输入梯形的上底："))
Bottom_line = float(input("请输入梯形的下底："))
high = float(input("请输入梯形的高："))
S = (Upper_sole + Bottom_line) * high / 2
print("梯形的面积为：", S)

print("-------- 题目12 --------")
# num = int(input("请输入一个整数："))
# if(num >= 10 and num <= 20):
#     print(f"数字 {num} 是否在10-20之间：True")
# else:
#     print(f"数字 {num} 是否在10-20之间：False")
num = int(input("请输入一个整数："))
result = num >= 10 and num <= 20
print(f"数字{num}是否在10-20之间：{result}")
