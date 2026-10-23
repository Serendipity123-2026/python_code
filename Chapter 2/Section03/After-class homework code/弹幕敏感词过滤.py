print("-------- 弹幕敏感词过滤 --------")
text = "这个视频太垃圾了，垃圾up主，质量垃圾差"
print(text)
count = text.count("垃圾")
print("敏感词出现次数为：", count)
new_text = text.replace("垃圾", "**")
print(new_text)