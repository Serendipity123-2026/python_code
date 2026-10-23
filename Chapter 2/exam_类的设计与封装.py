class BankAccount:
    bank_name = "软帝银行"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        if money < 0:
            print("存款金额必须大于0")
            return
        else:
            print(f"{self.owner} 存款 {money} 元成功")
            self.balance += money

    def withdraw(self, money):
        if money > self.balance:
            print(f"余额不足，当前余额 {self.balance} 元")
            return
        else:
            print(f"{self.owner} 取款 {money} 元成功")
            self.balance -= money

    def __str__(self):
        return f"账户名：{self.owner}，余额：{self.balance}元（{self.bank_name}）"


acc = BankAccount("张三", 1000)
acc.deposit(500)
acc.withdraw(2000)
acc.withdraw(300)
acc.deposit(-100)
print(acc)
