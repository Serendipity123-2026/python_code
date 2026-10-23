print("-------- 会员昵称规范化 --------")
nicknames = ["  Alice  ", "BOB", "  Charlie"]
str1, str2, str3 = nicknames
new_nicknames = [str1.strip().lower(), str2.strip().lower(), str3.strip().lower()]
print(new_nicknames)