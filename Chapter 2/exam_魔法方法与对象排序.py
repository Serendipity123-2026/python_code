class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}({self.score}分)"

    def __eq__(self, other):
        return self.name == other.name and self.score == other.score

    def __lt__(self, other):
        return self.score > other.score


stus = [Student("王林", 88), Student("李慕婉", 95), Student("韩立", 76), Student("紫灵", 92)]

stus.sort()
stus.reverse()
for s in stus:
    print(s, end=" ")
print()
print("最高分同学：", max(stus, key=lambda x: x.score))
s1 = Student("王林", 88)
print("s1与王林相等吗：", s1 == stus[1])
