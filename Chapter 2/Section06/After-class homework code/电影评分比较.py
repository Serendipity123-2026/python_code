"""
定义一个 Movie 类，包含片名和评分两个实例属性，
重写 __gt__ 魔法方法，按照评分比较两部电影的高低。
创建两部电影：《星际穿越》评分9.4，《盗梦空间》评分9.3，
用 > 比较并输出：星际穿越 的评分更高 或 盗梦空间 的评分更高

"""


class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __gt__(self, other):
        return self.rating > other.rating


movie1 = Movie("《星际穿越》", 9.4)
movie2 = Movie("《盗梦空间》", 9.3)

if movie1 > movie2:
    print(f"{movie1.title}的评分更高")
else:
    print(f"{movie2.title}的评分更高")