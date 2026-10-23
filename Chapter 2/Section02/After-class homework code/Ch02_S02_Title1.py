import math

print("-------- 题目1 --------")
height = float(input("请输入您的身高："))
weight = float(input("请输入您的体重："))
BMI = weight / (height ** 2)
# if BMI >= 18.5 and BMI <= 23.9:
if 18.5 <= BMI <= 23.9:
    print("体重正常")

print("-------- 题目2 --------")
string = input("请输入密码：")
if len(string) >= 8:
    print("密码强度：强")
else:
    print("密码强度：弱")

print("-------- 题目3 --------")
kilo = float(input("请输入行驶的里程数："))
price = 0
if kilo <= 2:
    price = 13
elif kilo <= 10:
    price = 13 + (kilo-2) * 2.3
else:
    price = 13 + 8 * 2.3 + (kilo-10) * 3.5
print(f"出租车费用：{price:.2f}元")

print("-------- 题目4 --------")
water_consumption = float(input("请输入这个月的用水量："))
price = 0
if water_consumption <= 12:
    price = water_consumption * 3.07
elif 12 < water_consumption <= 20:
    # 第一档 + 第二档
    price = (12 * 3.07) + (water_consumption - 12) * 4.07
else:
    # 第一档 + 第二档 + 第三档
    price =(12 * 3.07) + (8 * 4.07) + (water_consumption - 20) * 6.07
print(f"本月水费：{price}元")


print("-------- 题目5 --------")
lamp = input("请输入信号灯的颜色（红/黄/绿）：")
match True:
    case _ if lamp == "红":
        print("停止")
    case _ if lamp == "黄":
        print("减速慢行")
    case _ if lamp == "绿":
        print("通行")
    case _:
        print("信号异常")

print("-------- 题目6 --------")
month = int(input("请输入月份："))
match  month:
    case 3 | 4 | 5:
        print("春季")
    case 6 | 7 | 8:
        print("夏季")
    case 9 | 10 | 11:
        print("秋季")
    case 12 | 1 | 2:
        print("冬季")
    case _:
        print("月份不合法")

print("-------- 题目7 --------")
N = int(input("请输入一个正整数："))
while True:
    if N < 0:
        print("请重新输入")
        N = int(input("请输入一个正整数："))
    else:
        print(N)
        N -= 1
        if N == 0:
            print("发射！")
            break
print("-------- 题目8 --------")
# a = int(input("请输入第一个正整数："))
# b = int(input("请输入第二个正整数："))
# lcm = math.lcm(a,b)
# print(f"{a}和{b}的最小公倍数是：{lcm}")

a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))
max_num = max(a, b)
while True:
    if max_num % a == 0 and max_num % b == 0:
        break
    max_num += 1
print(f"{a}和{b}的最小公倍数是：{max_num}")

print("-------- 题目9 --------")
start = int(input("请输入起始数："))
stop = int(input("请输入结束数："))
sum = 0
for i in range(start,stop+1):
    if i % 2 == 0:
        sum += i
print(f"{start}到{stop}之间所有偶数这和：{sum}")


print("-------- 题目10 --------")
string = input("请输入一个英文字符串：")
count = 0
for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" \
        or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        count += 1
print("元音字母个数：", count)

print("-------- 题目11 --------")
N = int(input("请输入行数："))
for i in range(1,N+1):
    for j in range(1,N+1):
        print("*",end="")
    N -= 1
    print()

print("-------- 题目12 --------")
N = int(input("请输入行数："))
for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("-------- 题目13 --------")
sum = 0
for i in range(1,101):
    if i % 10 == 3 or i // 10 ==3:
        continue
    sum += i
print(sum)


print("-------- 题目14 --------")
balance = 1000.0
print("====== ATM菜单 ======")
print("1. 查询余额")
print("2. 存款")
print("3. 取款")
print("4. 退出")
print("====================")
while True:
    operation = int(input("请选择操作："))
    match operation:
        case 1:
            print(f"当前余额：{balance}元")
        case 2:
            money = float(input("请输入要存入的金额："))
            balance += money
            print(f"当前余额为{balance}元")
        case 3:
            take = float(input("请输入要取出的金额："))
            if take > balance:
                print(f"余额不足，当前余额为{balance}元")
            else:
                balance -= take
                print(f"当前余额为{balance}元")
        case 4:
            print("感谢使用，再见！")
            break


print("-------- 题目15 --------")
num = int(input("请输入一个正整数："))

for i in range(2, num+1):
    flag = 1
    for j in range(2, i):
        if i % j == 0:
            flag = 0
            break
    if flag:
        count += 1
