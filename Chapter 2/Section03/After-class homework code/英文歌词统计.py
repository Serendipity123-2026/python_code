print("-------- 英文歌词统计 --------")
lyric = "we will we will rock you rock you"
# count = 1
# for i in lyric:
#     if i == " ":
#         count = count + 1
# print(count)
words_lyric = lyric.split(" ")   # 以空格为分割，将字符串分成单词列表
# print(words_lyric)        # ['we', 'will', 'we', 'will', 'rock', 'you', 'rock', 'you']
count = len(words_lyric)
print(count)