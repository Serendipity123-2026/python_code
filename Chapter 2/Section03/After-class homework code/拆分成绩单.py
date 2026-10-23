print("-------- 拆分成绩单 --------")
scores = (92, 85, 78, 66, 95, 88, 73)
first, *middle, last = scores
print(first, middle, last)
mid_avg = round(sum(middle) / len(middle), 1)
print(mid_avg)
