# 收银找零计算器
# price = int(input("商品总价为："))
# cost = int(input("顾客付款金额为："))
# money = cost - price
#
# if money < 0:
#     print("付款金额不足！")
# else:
#     s_money = money
#     print(f"找零总额：{s_money}元")
#     # 并列if，不是嵌套
#     f = s_money // 50
#     s_money = s_money % 50
#     print(f"50元：{f}张")
#
#     t = s_money // 20
#     s_money = s_money % 20
#     print(f"20元：{t}张")
#
#     ten = s_money // 10
#     s_money = s_money % 10
#     print(f"10元：{ten}张")
#
#     five = s_money // 5
#     s_money = s_money % 5
#     print(f"5元：{five}张")
#
#     one = s_money // 1
#     s_money = s_money % 1
#     print(f"1元：{one}张")


# 斐波那契数列
# n = int(input("请输入n："))
# a, b = 1, 1
# for i in range(n):
#     print(a)
#     a, b = b, a+b




# 歌手大赛评分
# score = []
# count = 0
# for i in range(10):
#     nun = int(input(f"请输入第{i+1}位评委打分："))
#     score.append(nun)
#
# max_score = max(score)
# min_score = min(score)
# print(f"去掉的最高分：{max_score}，去掉的最低分：{min_score}")
#
# score.remove(max_score)
# score.remove(min_score)
# avg_score = sum(score) / len(score)
# print(f"最终得分：{avg_score:.2f}")
#
# for i in score:
#     if i > avg_score:
#         count += 1
# print(f"高于最终得分的打分：{count}个")








# 评论敏感词过滤
# sensitive_words = ("暴力", "垃圾", "诈骗")
# string = input("请输入评论：")
# new_string = ""
# for i in sensitive_words:
#     if string in sensitive_words:
#         pass







