"""
定义一个 BankAccount 类，包含户主姓名和余额两个实例属性（余额默认为0），提供：

deposit(amount)：存款，存款后输出当前余额
withdraw(amount)：取款，若余额不足输出"余额不足"，否则取款并输出当前余额

创建户主为"张三"、初始余额1000的账户，先存款500，再取款200，最后尝试取款1500，观察输出结果

"""


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"当前余额为；{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance -= amount
            print(f"当前余额为；{self.balance}")


acc = BankAccount("张三", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(1500)
