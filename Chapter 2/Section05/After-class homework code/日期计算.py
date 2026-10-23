from datetime import datetime as dt

date_input = input("输入一个日期（格式 YYYY-MM-DD，例如 2026-12-31）：")
date_time = dt.strptime(date_input, "%Y-%m-%d")
print(date_time)
today = dt.today()
print(today)

diff = date_time - today
print(f"{date_time}距离今天还剩{diff.days}")
