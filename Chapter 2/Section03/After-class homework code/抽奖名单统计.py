print("-------- 抽奖名单统计 --------")
first_prize = {"张三", "李四", "王五", "赵六"}
second_prize = {"王五", "钱七", "孙八", "李四"}

total_prize = first_prize | second_prize
print(f"参与抽奖的所有中奖用户总数：{len(total_prize)}")

two_prize = first_prize & second_prize
print(f"两轮都中奖的用户：{two_prize}")

one_prize = first_prize - second_prize
print(f"仅在第一轮中奖的用户：{one_prize}")

print("-------- 单词词频统计 --------")
sentence = "python is fun and python is powerful"
words_list = sentence.split()

words_dict = {}
for word in words_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

# for k, v in words_dict.items():
#     print(k, v)
print(words_dict)