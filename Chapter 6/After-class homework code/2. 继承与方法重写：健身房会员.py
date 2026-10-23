class Member:
    def __init__(self, name):
        self.name = name

    def get_fee(self):
        return 199

    def describe(self):
        return f"{self.name} 的会员费是 {self.get_fee()} 元"

class StudentMember:
    pass

class FamilyMember:
    pass