# class A:
#     def show(self):
#         print("A.show")
#
# class B:
#     def show(self):
#         print("B.show")
#
# class C(A, B):
#     pass
#
# c = C()
# c.show()
# print(C.__mro__)


class Dog():
    def eat(self):
        print("Dog.eat")

class Cat():
    def eat(self):
        print("Cat.eat")

    def attack(self):
        print("Cat.attack")
class Pig(Dog, Cat):
    def eat(self):
        print("pig.eat")


class Bird(Pig):
    def fly(self):
        print("Bird.fly")

if __name__ == '__main__':
    # p = Pig()
    # p.eat()
    # p.attack()
    b = Bird()
    b.attack()
    print(Bird.__mro__)
