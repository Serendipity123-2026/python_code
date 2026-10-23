"""
某商场举行抽奖活动，奖项列表如下：

    prizes = ["一等奖: 手机", "二等奖: 耳机", "三等奖: 保温杯", "谢谢参与"]

请使用 random.choice 编写程序，模拟 10 位顾客依次抽奖，每次打印顾客编号（1~10）和抽到的奖项。

"""

import random as rd

prizes = ["一等奖: 手机", "二等奖: 耳机", "三等奖: 保温杯", "谢谢参与"]

for i in range(1, 11):
    award = rd.choice(prizes)
    print(f"第{i}位顾客中了：{award}")