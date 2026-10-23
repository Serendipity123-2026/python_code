import random

staff = ["张伟", "王芳", "李娜", "刘强", "陈静",
         "杨洋", "赵磊", "黄敏", "周杰", "吴婷"]
winners = random.sample(staff, 3)
prize = ["一等奖", "二等奖", "三等奖"]

for prize, name in zip(prize, winners):     # `zip()` 是 Python 内置函数，**把多个序列按位置一一配对打包**
    print(f"{prize}获得者:{name}")

