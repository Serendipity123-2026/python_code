class Father:
    def eat(self):
        print("Father eating")
        print("吃饭")


class Body(Father):
    def eat(self):
        super().eat()
        print("喝奶")

if __name__ == '__main__':
    body = Body()
    body.eat()