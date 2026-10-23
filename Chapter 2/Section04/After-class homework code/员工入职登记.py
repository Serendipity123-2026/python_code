"""
定义函数 register_employee(name, age, position, city)，打印并返回员工信息字典。

要求用三种方式分别调用：

1. 全部使用位置参数：("赵敏", 26, "测试工程师", "武汉")
2. 全部使用关键字参数（顺序打乱）
3. 位置参数与关键字参数混用

"""

print("-------- 停车费计算器（默认参数） --------")


def register_employee(name, age, position, city):
    employee = {'name': name, 'age': age, 'position': position, 'city': city}
    return employee


print(register_employee("赵敏", 26, "测试工程师", "武汉"))
print(register_employee(city="广州", position="架构师", age=28, name="张三"))
print(register_employee("李四", 26, city="上海", position="测试工程师"))