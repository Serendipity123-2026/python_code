# list1 = [1,2,3,4]
# list2 = [3,7,8,9]
#
# list3 = list1 + list2
# # list3 = [*list1, *list2]
# for i in list3:
#     print(i)


# 用户输入的10个数字，存储到一个列表中，
# 并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。
# num = []
# for i in range(5):
#     number = int(input(f"请输入{i+1}个数："))
#     num.append(number)
#
# num.sort()
# print(num)
# print(f"列表中的最小值为：{min(num)}，列表中的最大值为：{max(num)}")
# avg = sum(num) / len(num)
# print(f"平均值为：{avg}")


# 合并两个列表中的元素，并对合并的结果进行去重处理
# num1 = [1,2,3,4,5]
# num2 = [2,3,8,9,10]
#
# new_num1 = num1 + num2
#
# new_num2 = []
# for i in new_num1:
#     if i not in new_num2:
#         new_num2.append(i)
# print(new_num2)

# 生成1-20的平方列表
# num = []
# sqrt = 1
# for i in range(1,21):
#     sqrt = i ** 2
#     num.append(sqrt)
# print(num)

# sqrt = [(i ** 2) for i in range(1,21)]
# print(sqrt)

# 提取所有偶数，并计算其平方
# sqrt = [(i ** 2) for i in range(1,21) if i % 2 == 0]
# print(sqrt)


# 将多个列表合并为一个列表，
# 去重重复元素，排好序（升序）后输出到控制台
# num1, num2, num3 = [2, 1, 3], [3, 5, 4], [4, 5, 6]
# total_num = num1 + num2 + num3
# new_num = []
# for i in total_num:
#     if i not in new_num:
#         new_num.append(i)
# print(new_num)
# new_num.sort()
# print(new_num)


# s = "     Hello-Python-Hello-World     "
# slist = s.split("-")
# print(slist)

# s = "  Hello-Python-World  "
# t = s.strip()
# print(t.split("-"))
# print(t.replace("-", "@"))
# print(t.count("o"))
# print(t.lower().startswith("hello"))


# s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
# print(len(s))
# s.append(10)
#
# print(s)
# print(len(s))
#
# s.insert(2, 23)
# print(s)
# print(len(s))
#
# s.remove(100)
# print(s)
# print(len(s))
#
# s.pop()
# print(s)
# print(len(s))
#
# s.pop(0)            # pop() 中放的是索引
# print(s)
# print(len(s))
#
# s.sort()
# print(s)
#
#
# s.reverse()
# print(s)
# list1 = [i ** 2 for i in range(1, 21) if i % 2 == 0]
# print(list1)

# list1, list2, list3 = [1, 2, 3], [3, 4, 5], [5, 6, 7]
# total = [*list1, *list2, *list3]
# print(total)
# uni_list = []
#
# for i in total:
#     if i not in uni_list:
#         uni_list.append(i)
#
# print(uni_list)

# mail = input("请输入邮箱：")
# if mail.count("@") == 1 and mail.count(".") >=1:
#     print("合法")
# else:
#     print("不合法")


# str = input("请输入字符串:")
# if str == str[::-1]:
#     print("yes")
# else:
#     print("no")

# list = []
# for i in range(3):
#     str = input("  :")
#     new_str = str[::-1].upper()
#     list.append(new_str)
# print(list)


# students = (
#     ("S001", "王林", 85, 92, 78),
#     ("S002", "李慕婉", 92, 88, 95),
#     ("S003", "十三", 78, 85, 82),
#     ("S004", "曾牛", 88, 79, 91),
#     ("S005", "周轶", 95, 96, 89),
#     ("S006", "王卓", 76, 82, 77),
#     ("S007", "红蝶", 89, 91, 94),
#     ("S008", "徐立国", 75, 69, 82),
#     ("S009", "许木", 86, 89, 98),
#     ("S010", "遁天", 66, 59, 72)
# )
#
# for student in students:
#     score = student[2] + student[3] + student[4]
#     print(score)
#
# chinese_list = [student[2] for student in students]
# avg_chinese = round(sum(chinese_list) / len(chinese_list), 1)
# print(avg_chinese)
# math_list = [student[3] for student in students]
# avg_math = round(sum(math_list) / len(math_list), 1)
# print(avg_math)
# english_list = [student[4] for student in students]
# avg_english = round(sum(english_list) / len(english_list), 1)
# print(avg_english)
#
#
# min_chinese_score =min(chinese_list)
# max_chinese_score =max(chinese_list)
# avg_chinese_score =round(sum(chinese_list) / len(chinese_list), 1)
# print(min_chinese_score)
# print(max_chinese_score)
# print(avg_chinese_score)
#
# min_math_score =min(math_list)
# max_math_score =max(math_list)
# avg_math_score =round(sum(math_list) / len(math_list), 1)
# print(min_math_score)
# print(max_math_score)
# print(avg_math_score)
#
# min_english_score =min(english_list)
# max_english_score =max(english_list)
# avg_english_score =round(sum(english_list) / len(english_list), 1)
# print(min_english_score)
# print(max_english_score)
# print(avg_english_score)

# list1 = [1, 2, 3, "hello", True, None, [1, 2, 3]]
# # 删除元素
# del list1[0]    # [2, 3, 'hello', True, None, [1, 2, 3]]

# num1, num2 = [12, 11, 13], [13, 15, 14]
# set1 = {*num1, *num2}
# print(set1)
# print(type(set1))


# # 选修足球学生名单
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# # 选修篮球学生名单
# basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# # 选修法语学生名单
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# # 选修艺术学生名单
# art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
#
# # 选修了 法语 和 艺术
# f_a_set = french_set & art_set
# # 选修了所有四门
# four_set = french_set & basketball_set & football_set & art_set
# # 选修了足球, 但是没有选修篮球
# f_set = football_set - basketball_set
#
# # 学生名单
# student_set = football_set | basketball_set | french_set | art_set
#
# print(student_set)
#
# all_union_list = [*football_set , *basketball_set , *french_set , *art_set ]
# print(all_union_list)
#
# for student in student_set:
#     print(all_union_list.count(student))


# shopping_cart = {}
# menu = """
# ########### 购物车系统 ##########
# #         1. 添加购物车         #
# #         2. 修改购物车         #
# #         3. 删除购物车         #
# #         4. 查询购物车         #
# #         5. 退出购物车         #
# ###############################
# """
# print("欢迎使用购物车管理系统 ~")
#
# while True:
#     print(menu)
#     operation = int(input("请输入操作："))
#     if operation == 1:
#         goods_name = input("请输入商品名称：")
#         price = float(input("请输入商品价格"))
#         number = int(input("请输入商品数量"))
#         shopping_cart[goods_name] = {"price": price, "number": number}
#     elif operation == 2:
#         goods_name = input("请输入商品名称：")
#         if goods_name in shopping_cart:
#             price = float(input("请输入商品价格"))
#             number = int(input("请输入商品数量"))
#             shopping_cart[goods_name] = {"price": price, "number": number}
#     elif operation == 3:
#         goods_name = input("请输入要删除的商品名称：")
#         if goods_name in shopping_cart:
#             del shopping_cart[goods_name]
#     elif operation == 4:
#         for goods_name in shopping_cart.keys():
#             goods_info = shopping_cart[goods_name]
#         print(f"商品名称：{goods_name}，商品价格：{goods_info['price']}，商品数量：{goods_info['number']}。")
#     elif operation == 5:
#         break
#     else:
#         print("错误输入")
#     print(shopping_cart)
#
# s1 = {15, 13, 12, 10, 19}
# print(s1)       # {19, 10, 12, 13, 15} 乱序
# s1.clear()
# print(s1)       # set()


# 教务管理系统
# 教务管理系统
menu = """
【菜单】
1. 添加学生信息   2. 修改学生信息   3. 删除学生信息
4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统
"""

# 记录所有学员成绩信息
students = {"张三": {'chinese_score': 90, 'math_score': 90, 'english_score': 89},
            "李四": {'chinese_score': 89, 'math_score': 97, 'english_score': 79},
            "王五": {'chinese_score': 91, 'math_score': 76, 'english_score': 83}}
while True:
    print(menu)
    choice = int(input("请输入操作(1-7)："))
    match choice:
        case 1:
            name = input("请输入学生姓名：")
            chinese_score = float(input("请输入学生语文成绩："))
            math_score = float(input("请输入学生数学成绩："))
            english_score = float(input("请输入学生英语成绩："))
            students[name] = {'chinese_score': chinese_score,
                              'math_score': math_score,
                              'english_score': english_score}
            print(f"学生{students[name]}成绩添加成功！")
        case 2:
            name = input("请输入要修改的学生姓名：")
            if name not in students:
                print("学生不存在！")
            else:
                chinese_score = float(input("请输入学生语文成绩："))
                math_score = float(input("请输入学生数学成绩："))
                english_score = float(input("请输入学生英语成绩："))
                students[name] = {'chinese_score': chinese_score,
                                  'math_score': math_score,
                                  'english_score': english_score}
                print(f"学生{students[name]}成绩修改成功！")
        case 3:
            if len(students) == 0:
                print("无学生信息！")
            else:
                name = input("请输入要删除的学生姓名：")
                del students[name]
                print(f"学生{students[name]}信息删除成功！")
        case 4:
            if len(students) == 0:
                print("无学生信息！")
            else:
                name = input("请输入要查询的学生姓名：")
                for k, v in students.items():
                    print(
                        f"学生{k}的语文成绩为{v['chinese_score']}\t数学成绩为{v['math_score']}\t英语成绩为{v['english_score']}")
        case 5:
            if len(students) == 0:
                print("无学生信息！")
            else:
                for k, v in students.items():
                    print(
                        f"学生{k}的语文成绩为{v['chinese_score']}\t数学成绩为{v['math_score']}\t英语成绩为{v['english_score']}")
        case 6:
            if len(students) == 0:
                print("无学生信息！")
            else:
                chinese_list, math_list, english_list = [], [], []
                for k, v in students.items():
                    chinese_list.append(v['chinese_score'])
                    math_list.append(v['math_score'])
                    english_list.append(v['english_score'])
                avg_chinese = round(sum(chinese_list) / len(chinese_list), 2)
                avg_math = round(sum(math_list) / len(math_list), 2)
                avg_english = round(sum(english_list) / len(english_list), 2)
                print(f"语文成绩最高分为{max(chinese_list)}, 最低分为{min(chinese_list)}, 平均分为{avg_chinese}")
                print(f"数学成绩最高分为{max(math_list)}, 最低分为{min(math_list)}, 平均分为{avg_math}")
                print(f"英语成绩最高分为{max(english_list)}, 最低分为{min(english_list)}, 平均分为{avg_english}")

                for name in students:
                    pass
        case 7:
            print("系统退出成功")
            break
        case _:
            pass
