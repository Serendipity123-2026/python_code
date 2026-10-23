print("-------- 通讯录管理系统 --------")
contacts = {"张三": {"phone": "13812345678", "city": "北京"}}
menu = """
    1.添加联系人         2.查询联系人      3.删除联系人
    4.列出所有联系人      5.统计           6.退出系统
"""

while True:
    print(menu)
    operation = int(input("请选择操作："))
    if operation == 1:
        name = input("请输入姓名：")
        if name in contacts:
            print("联系人已存在")
        else:
            phone = input("请输入电话：")
            city = input("请输入城市：")
            contacts[name] = {"phone": phone, "city": city}
            print("添加联系人成功！")
    elif operation == 2:
        name = input("请输入姓名：")
        if name not in contacts:
            print("联系人不存在")
        else:
            key = contacts[name]
            print(f"电话为：{key['phone']}")
            print(f"所在城市为：{key['city']}")
    elif operation == 3:
        name = input("请输入姓名：")
        if name not in contacts:
            print("联系人不存在")
        else:
            del contacts[name]
            print("联系人删除成功！")
    elif operation == 4:
        if not contacts:
            print("通讯录为空")
        else:
            for k, v in contacts.items():
                print(f"{k}的电话为：{v['phone']}")
                print(f"{k}所在城市为{v['city']}")

    elif operation == 5:
        name_num = len(contacts)
        if name_num == 0:
            print("通讯录为空！")
        else:
            print(f"通讯录中的联系人总数为：{name_num}")

    elif operation == 6:
        print("系统退出成功！")
        break
    else:
        print("错误输入")