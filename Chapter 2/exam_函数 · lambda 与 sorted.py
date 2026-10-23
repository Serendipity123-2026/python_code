scores = {"王林": 88, "李慕婉": 95, "韩立": 76, "紫灵": 92, "许立国": 60}
new_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(new_scores)

top3 = new_scores[0:3]
print("成绩排行榜（前三名）:")
