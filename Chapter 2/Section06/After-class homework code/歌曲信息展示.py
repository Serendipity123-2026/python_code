"""
定义一个 Song 类，包含歌名、歌手、时长（分钟）三个实例属性，
重写 __str__ 魔法方法，
返回格式如：《晴天》 - 周杰伦 (4分29秒)。
创建对象并使用 print() 直接打印，观察输出

"""



class Song:
    def __init__(self, song_title, artist, duration):
        self.song_title = song_title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"《{self.song_title}》 - {self.artist} ({self.duration})"


song = Song("晴天", "周杰伦", "4分29秒")
print(song)
