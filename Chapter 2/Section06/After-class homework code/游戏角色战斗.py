class Hero:
    def __init__(self, role_name, attack_power, hit_points=100):
        self.role_name = role_name
        self.attack_power = attack_power
        self.hit_points = hit_points

    def attack(self, other):
        other.hit_points =other.hit_points - self.attack_power
        print(f"{other.role_name}受到了{self.attack_power}点伤害，剩余血量{other.hit_points}")

    def is_alive(self):
        return self.hit_points > 0


hero1 = Hero("亚瑟", 30)
hero2 = Hero("鲁班", 50)
hero1.attack(hero2)
print(hero2.is_alive())
