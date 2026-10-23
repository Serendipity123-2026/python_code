print("-------- 一周气温记录 --------")
temps = (26, 31, 26, 19, 24, 31, 22)

print(f"气温 26 出现的次数：{temps.count(26)}")
print(f"气温 31 第一次出现的位置（索引）：{temps.index(31)}")
print(f"前三天的气温切片：{temps[:3]}")
print(f"一周最高气温：{max(temps)}")
print(f"一周最低气温：{min(temps)}")
print(f"一周平均气温：{round(sum(temps) / len(temps), 1)}")