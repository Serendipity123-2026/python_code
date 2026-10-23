import csv

with open("./data/01.csv", "w", encoding="utf-8", newline="") as f:
    dict_writer = csv.DictWriter(f, fieldnames=["name", "age", "sex", "score"])
    dict_writer.writeheader()
    dict_writer.writerows([
        {"name": "张三", "age": 18, "sex": "男", "score": 89},
        {"name": "李四", "age": 18, "sex": "女", "score": 99},
        {"name": "王五", "age": 19, "sex": "男", "score": 91},
    ])
