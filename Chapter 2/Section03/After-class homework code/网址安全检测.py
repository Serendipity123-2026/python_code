print("-------- 网址安全检测 --------")
urls = ["https://www.ruandi.com", "http://test.cn", "http://mail.qq.com", "ftp://old.org"]
count = 0
for i in urls:
    if i.startswith("https://"):
        print(f"{i} 该网址是安全网址")
        count += 1
    else:
        print(f"{i} 该网址是不安全网址")
print("安全网址的数量是：", count)