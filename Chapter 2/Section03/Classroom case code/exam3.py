# 温度转换函数
# def c_to_f(c):
#     f = (c * 9 / 5) + 32
#     print(f"{c} 摄氏度 = {round(f, 1)} 华氏度")
#
# def f_to_c(f):
#     c = (f - 32) * 5 / 9
#     print(f"{f} 华氏度 = {round(c, 1)} 摄氏度")
#
#
# c_to_f(37)
# f_to_c(98.6)


# 手机号脱敏函数
# def mask_phone(phone):
#     if len(phone) == 11:
#         w_phone = phone[:3] + "****" + phone[7:]
#         print(w_phone)
# phone  = input("请输入手机号：")
# mask_phone(phone)

# 员工薪资统计
# salaries = { "张三": 8500,
#              "李四": 9200,
#              "王五": 7800,
#              "赵六": 10500}
# max_name = max(salaries, key=salaries.get)
# print(f"最高薪员工：{max_name}，薪资：{salaries.get(max_name)}")
#
#
# for k, v in salaries.items():
#     salaries[k] = round(v * 1.1, 1)
# print(f"涨薪后：{salaries}")
# avg_salary = round(sum(salaries.values()) / len(salaries.values()), 1)
# print(f"涨薪后平均薪资：{avg_salary}元")


# 用户活跃分析
# yesterday = {"user01", "user02", "user03", "user04"}
# today = {"user02", "user03", "user05", "user06"}
# two_login = yesterday & today
# print(f"连续两天都活跃：{two_login}")
# add_login = today - yesterday
# print(f"今日新增活跃：{add_login}")
# lose_login = yesterday - today
# print(f"今日流失用户：{lose_login}")
# total_login = yesterday | today
# count = 0
# for i in total_login:
#     count += 1
# print(f"两天内活跃过的用户总数：{count}")


# 成绩排行榜
students = [("韩立", 78), ("王林", 92), ("李慕婉", 88), ("曾牛", 64), ("紫灵", 95)]
students.sort(key = lambda x:x[1])
students.reverse()
print(students)

print("成绩怕排行榜：")
count = 1
for student in students[:3]:
    print(f"第{count}名：{student[0]} {student[1]}分")
    count += 1

name_list = [student[0] for student in students if student[1] >= 80]
print(name_list)