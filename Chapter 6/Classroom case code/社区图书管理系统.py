from abc import ABC, abstractmethod  # 引入抽象类和抽象方法
import json


# 图书类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id  # 书籍编号
        self.title = title  # 书籍标题
        self.author = author  # 作者
        self.total_num = total_num  # 总数量


# 会员类(普通会员和VIP会员的父类)   ABC 抽象类  让子类继承时 要强制重写抽象方法
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id  # 会员卡号
        self.name = name  # 会员姓名
        self.__password = password  # 会员密码

    # 获取密码方法
    def get_password(self):
        return self.__password

    # 普通会员和VIP会员的借阅数量限制 计算方式不同,所以定义为抽象方法
    @abstractmethod
    def get_borrow_limit(self):
        pass


# 普通会员类(继承自会员类)
class NormalMember(Member):
    def __init__(self, member_id, name, password):
        super().__init__(member_id, name, password)  # 调用父类的构造方法

    # 重写父类的抽象方法  普通会员最多可借书3本
    def get_borrow_limit(self):
        return 3


# VIP会员类(继承自会员类)
class VipMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)  # 调用父类的构造方法
        self.vip_level = vip_level  # VIP等级

    # 重写父类的抽象方法  VIP会员最多可借书(6+vip_level)本
    def get_borrow_limit(self):
        return 6 + self.vip_level


# 图书管理系统类
class LibrarySystem:
    def __init__(self):
        self.books = {}  # 图书字典
        self.members = {}  # 会员字典
        self.borrow_records = {}  # 借阅记录字典 {图书编号: 借阅数量}

        # Member：表示这个变量正常情况下存 Member 类的实例（登录成功）  None：表示这个变量为空（未登录）
        self.current_member: Member | None = None  # 当前登录的会员

        # 当创建LibrarySystem对象时，自动加载图书列表信息
        self.load_books_data()

        self.load_members_data()

    # 加载book.json文件中的图书列表信息，并添加到self.books中
    def load_books_data(self):
        with open('./data/books.json', 'r', encoding='utf-8') as f:
            books_data = json.load(f)  # 加载图书数据

            # 遍历books.json中的图书信息
            for book_data in books_data:
                # 实例化每本图书
                book = Book(book_data['编号'], book_data['标题'], book_data['作者'], book_data['数量'])
                # 将每本book添加到图书字典中  {图书编号: 图书对象}
                self.books[book_data['编号']] = book
            print("图书数据加载完成！")

    # 加载members.json文件中的会员列表信息，并添加到self.members中
    def load_members_data(self):
        with open('./data/members.json', 'r', encoding='utf-8') as f:
            members_data = json.load(f)  # 加载会员数据
            # 遍历members.json中的会员信息
            for member_data in members_data:
                # 判断会员等级，实例化不同类型的会员
                if '会员等级' in member_data:
                    # 将members.json文件中的信息以
                    # {member_id: member_data['卡号'], name: member_data['姓名'], password: member_data['密码'], vip_level: member_data['会员等级']}
                    member = VipMember(member_data['卡号'], member_data['姓名'], member_data['密码'],
                                       member_data['会员等级'])  # 创建VIP会员对象
                    # 将会员对象添加到会员字典中  {会员卡号: 会员对象}
                    self.members[member_data['卡号']] = member
                else:
                    # 将members.json文件中的信息以 {member_id: member_data['卡号'], name: member_data['姓名'], password: member_data['密码']}
                    member = NormalMember(member_data['卡号'], member_data['姓名'], member_data['密码'])  # 创建普通会员对象
                    self.members[member_data['卡号']] = member
            print("会员数据加载完成！")

    def run(self):
        while True:
            print("--------------- 欢迎使用社区图书管理系统！---------------")
            member_id = input("请输入会员卡号：")  # 获取会员卡号
            # 判断会员卡号是否在会员字典中
            if member_id in self.members:
                password = input("请输入密码：")  # 获取密码
                # self.members[member_id]：根据卡号取出对应的会员对象   .get_password()：调用会员对象的方法，获取保存的密码
                if self.members[member_id].get_password() == password:
                    # 登录成功，将当前会员对象赋值给self.current_member
                    self.current_member = self.members[member_id]
                    print(f"欢迎{self.current_member.name}登录！")
                    self.main_menu()
                    break
                else:
                    print("密码错误！")
                    continue  # 密码错误，继续循环
            else:
                print("会员卡号不存在！")

    # 主菜单
    def main_menu(self):
        while True:
            print("--------------- 系统主菜单 ---------------")
            print("1. 借阅图书")
            print("2. 归还图书")
            print("3. 查询所有图书")
            print("4. 查询我的借阅")
            print("5. 退出系统")
            choice = int(input("请输入你的选择："))

            match choice:
                case 1:
                    # 借阅图书
                    self.borrow_book()
                case 2:
                    # 归还图书
                    self.return_book()
                case 3:
                    # 查询所有图书
                    self.query_all_books()
                case 4:
                    # 查询我的借阅
                    self.show_borrowed_books()
                case 5:
                    print("感谢使用 再见！")
                    break
                case _:
                    print("无效的选择 请重新输入！")

    # 借阅图书
    def borrow_book(self):
        print("----------借阅图书----------")
        # 遍历图书字典中的每本图书
        for book in self.books.values():
            print(f"编号：{book.book_id}， 标题：{book.title}， 作者：{book.author}， 数量：{book.total_num}")
        book_id = input("请输入要借阅的图书编号：")
        # 判断图书编号是否在图书字典中
        if book_id in self.books:
            # 获取借阅数量
            borrow_num = int(input("请输入借阅数量："))
            # 判断借阅数量是否足够   self.books[book_id]获取图书对象   通过图书对象 .total_num获取图书数量
            if self.books[book_id].total_num < borrow_num:
                print("图书数量不足！ 请重新输入借阅数量！")
                return
            # 获取会员已借阅的总数量
            total_borrowed_num = sum(self.borrow_records.values())
            # 判断会员可借阅数量是否超出限制
            if (total_borrowed_num + borrow_num) > self.current_member.get_borrow_limit():
                print("超出借阅数量限制！ 请重新输入借阅数量！")
                return

            # 判断图书数量是否足够
            if borrow_num > self.books[book_id].total_num:
                print("图书数量不足！ 请重新输入借阅数量！")
                return

            # 更新图书数量
            self.books[book_id].total_num -= borrow_num
            # 判断当前   book_id 的图书是否之前已经被借阅过
            if book_id in self.borrow_records:
                # 如果之前借阅过，则更新借阅数量
                self.borrow_records[book_id] += borrow_num
            else:
                # 如果之前没有借阅过，则添加到借阅记录中
                self.borrow_records[book_id] = borrow_num
            print(f"借阅成功！剩余数量： {self.books[book_id].total_num}")
        else:
            print("图书编号不存在！")

    # 归还图书
    def return_book(self):
        print("----------归还图书----------")
        # 遍历借阅记录中的每条记录  borrow_records字典 -> {图书编号: 借阅数量}
        for book_id, borrow_num in self.borrow_records.items():
            book = self.books[book_id]
            print(f"编号：{book.book_id}， 标题：{book.title}， 作者：{book.author}， 借阅数量：{borrow_num}")

            return_num_id = input("请输入归还图书的编号：")
            # 判断归还图书的编号是否在借阅记录中
            if return_num_id in self.borrow_records:
                # 获取归还数量
                return_num = int(input("请输入归还数量："))
                # 判断归还数量是否超出借阅数量
                if return_num <= self.borrow_records[return_num_id]:
                    # 将归还数量添加到图书数量中
                    self.books[return_num_id].total_num += return_num
                    # 更新借阅记录中的借阅数量    borrow_records[return_num_id]获取到的是借阅数量
                    self.borrow_records[return_num_id] -= return_num
                    print(f"归还成功！ 剩余数量：{self.borrow_records[return_num_id]}")
                else:
                    print("归还数量超出借阅数量！请重新输入！")
            else:
                print("图书编号不存在！")

    # 查询所有图书
    def query_all_books(self):
        print("----------查询所有图书----------")
        # 遍历图书字典中的每本图书
        for book in self.books.values():
            print(f"编号：{book.book_id}， 标题：{book.title}， 作者：{book.author}， 数量：{book.total_num}")

    # 查询我的借阅
    def show_borrowed_books(self):
        print("----------查询我的借阅----------")
        # borrow_records 字典中只有编号和借阅数量 {book_id: borrow_num}
        for book_id, borrow_num in self.borrow_records.items():
            book = self.books[book_id]  # books字典为 {图书编号: 图书对象}      通过books[book_id] 获取图书对象
            print(f"编号：{book.book_id}， 标题：{book.title}， 作者：{book.author}， 数量：{borrow_num}")


if __name__ == '__main__':
    library_system = LibrarySystem()
    library_system.run()
