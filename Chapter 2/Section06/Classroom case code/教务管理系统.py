class Student:
    """ 学生类，有姓名和三科成绩 """
    def __init__(self, name, c_score, m_score, e_score):
        self.name = name
        self.c_score = c_score
        self.m_score = m_score
        self.e_score = e_score

    def __str__(self):
        return f"学生{self.name}，语文成绩：{self.c_score}\t数学成绩：{self.m_score}\t英语成绩：{self.e_score}\t总分：{self.c_score + self.m_score + self.e_score}"


class EduManagement:
    """ 教务管理类，实现增删改查学生成绩 """
    def __init__(self):
        self.stu_dict = {}

    @staticmethod
    def _is_valid_score(score: int) -> bool:
        return 0 <= score <= 100

    # 添加学生成绩
    def add_stu_score(self):
        name = input("请输入学生姓名；")
        # 判断学生是否存在
        if name in self.stu_dict:
            print("学生已存在")
            return

        c_score = int(input("请输入语文成绩："))
        if not self._is_valid_score(c_score):
            print("输入错误")
            return
        m_score = int(input("请输入数学成绩："))
        if not self._is_valid_score(m_score):
            print("输入错误")
            return
        e_score = int(input("请输入英语成绩："))
        if not self._is_valid_score(e_score):
            print("输入错误")
            return
        self.stu_dict[name] = Student(name, c_score, m_score, e_score)

    def mod_stu_score(self):
        name = input("请输入要修改的学生姓名；")
        if name not in self.stu_dict:
            print("学生不存在")
            return
        mod_c_score = int(input("请输入修改后的语文成绩："))
        if not self._is_valid_score(mod_c_score):
            print("输入错误")
            return
        mod_m_score = int(input("请输入修改后的数学成绩："))
        if not self._is_valid_score(mod_m_score):
            print("输入错误")
            return
        mod_e_score = int(input("请输入修改后的英语成绩："))
        if not self._is_valid_score(mod_e_score):
            print("输入错误")
            return
        self.stu_dict[name] = Student(name, mod_c_score, mod_m_score, mod_e_score)
        print("修改成功")

    def del_stu_score(self):
        name = input("请输入要查找的学生姓名；")
        if name not in self.stu_dict:
            print("学生不存在")
            return
        del self.stu_dict[name]
        print("删除成功")

    def search_stu_score(self):
        name = input("请输入要查找的学生姓名；")
        if name not in self.stu_dict:
            print("学生不存在")
            return
        print(self.stu_dict[name])

    def show_stu_score(self):
        for key, value in self.stu_dict.items():
            print(value)

    def run(self):
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生   2.修改学生   3.删除学生   4.查询指定学生   5.查询所有学生   6.退出系统  #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            choice = int(input("请选择要执行的操作, 输入1-6: "))

            try:
                match choice:
                    case 1:
                        self.add_stu_score()
                    case 2:
                        self.mod_stu_score()
                    case 3:
                        self.del_stu_score()
                    case 4:
                        self.search_stu_score()
                    case 5:
                        self.show_stu_score()
                    case 6:
                        print("退出系统")
                        break
                    case _:
                        print("输入错误，请重新选择")
            except ValueError:
                print("输入的数据有问题, 请检查, 然后重新输入 !!!")
            except Exception:
                print("程序运行出错了, 请重新选择 ~")


if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()