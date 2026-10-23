class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 10:
            self.__balance += amount
            print(f"存款后余额：{self.__balance}")
        else:
            print("存款金额必须大于10")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("余额不足")
        else:
            self.__balance -= amount
            print(f"取款后余额：{self.__balance}")

    def get_balance(self):
        return self.__balance


if __name__ == '__main__':
    acc = BankAccount("张三", 100)
    acc.deposit(50)  # 存款后余额：150
    acc.withdraw(30)  # 取款后余额：120
    print(acc.get_balance())  # 120
    acc.withdraw(500)  # 余额不足