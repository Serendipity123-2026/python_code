# # 计算圆的面积
# import math
#
#
# def circle_area(r: float) -> float:
#     area = 3.14 * r * r
#     return area
#
#
# area = circle_area(10)
# print(f"圆的面积为{area}")
#
#
#
# def circle_area_c(r: float) -> float:
#     s = 3.14 * r * r
#     c = 2 * 3.14 * r
#     return s, c
#
#
# al = circle_area_c(5)
# print(al)
# print(type(al))
#
# area, c = circle_area_c(5)
# print(area, c)


# def triangle_area(base, height):
#     """
#     计算三角形的面积
#     :param base: 三角形的底
#     :param height:  三角形的高
#     :return: 三角形的面积
#     """
#     return base * height / 2
#
#
# print(f"三角形的面积为{triangle_area(30, 20)}")


# def count_aeiou(s):
#     """
#     统计字符串中元音字母的个数
#     :param s: 字符串
#     :return: 元音字母个数
#     """
#     count = 0
#     for word in s:
#         if word in "aeiouAEIOU":
#             count += 1
#     return count
#
# print(count_aeiou("hello python hello world ok"))


# def calc_score(score_list):
#     """
#     计算成绩列表最高分，最低分，平均分
#     :param score_list: 分数列表
#     :return: 最高分，最低分，平均分
#     """
#
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list) / len(score_list), 1)
#     return max_s, min_s, avg_s
#
# s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
#
# print(calc_score(s_list))


# def calc_grade(score):
#     """
#     分数评级
#     :param score: 分数
#     :return: 等级
#     """
#     if score >= 90:
#         print("A")
#     elif score >= 75:
#         print("B")
#     elif score >= 60:
#         print("C")
#     else:
#         print("D")
#
#
# calc_grade(89)


# def is_palindrome(s):
#     """
#     回文字符串判断
#     :param s:
#     :return:
#     """
#     return s == s[::-1]
#
#
# print(is_palindrome("level"))


# def time_change(s):
#     """
#     时间转换
#     :param s: 秒数
#     :return: 时分秒
#     """
#     hours = s // 3600
#     minutes = (s -hours * 3600) // 60
#     seconds = s - hours * 3600 - minutes * 60
#     return hours, minutes, seconds
#
# print(time_change(10000))


# def determine_triangle_type(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         if a == b and b == c:
#             print("等边三角形")
#         elif a == b or b == c or a == c:
#             print("等腰三角形")
#         else:
#             print("普通三角形")
#     else:
#         print("不是三角形")


s = "PyThon"
for c in s:
    if c.isupper():
        print(f"{c} 是大写字母")
    elif c.islower():
        print(f"{c} 是小写字母")

