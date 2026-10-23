print("-------- 演出节目单管理 --------")
program = ["开场舞", "独唱", "小品", "魔术", "压轴合唱"]
for i in program:
    print(i)
print("--------------------------------------")
program.insert(0,"主持人致辞")
for i in program:
    print(i)
print("--------------------------------------")
program.remove("魔术")
for i in program:
    print(i)
print("--------------------------------------")
program.insert(3,"相声")
for i in program:
    print(i)
print("--------------------------------------")
count = 0
for i in program:
    count += 1
print("节目单上的节目总数为", count)