import math

num1 = float(input("第一个数："))
num2 = float(input("第二个数："))
num3 = float(input("第三个数："))

avg = (num1 + num2 + num3) / 3
print(avg)

up = float(input("up"))
down = float(input("down"))
high = float(input("high"))
S = (up + down) * high / 2
print(S)

r = float(input("r"))
C = 2 * math.pi * r
S = math.pi * r ** 2
print(C,S)

weight = float(input("weight"))
height = float(input("height"))
bmi = weight / (height ** 2)
print(bmi)