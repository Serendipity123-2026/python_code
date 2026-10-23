import json

data = {"name": "张三", "age": 18, "score": 99.5}
f = open("date.json", "w", encoding="utf-8")
json.dump(data, f, ensure_ascii=False, indent=2)
f.close()
