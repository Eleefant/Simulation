from Entitys import Entity


# edibility = 0 не съедобен = 1 съедобен для травоядных, 2 съедобен для хищников
class Creature(Entity):
    def __init__(self, picture, edibility, attack, hp=0, speed=0):
    #def __init__(self, hp, speed):
        super().__init__(picture, edibility)
        self.hp = hp
        self.speed = speed
        self.attack = attack


    def make_move(self):
        pass

    def eat_it(self):
        pass


class Herbivore(Creature):
    def __init__(self, attak):
        super().__init__('H', 2, 1, 5, 1)
        #super().__init__(5, 1)
        #self.picture = picture
        #self.edibility = edibility


class Predator(Creature):
    def __init__(self, picture='P', edibility=0):
        super().__init__('P', 0, 2, 10, 2)
        #super().__init__(10, 2)
        #self.picture = picture
        #self.edibility = edibility



x = Predator
print(x.__dict__)











    #def get_param(self):
    #    print(f'параметры кричура {self.picture} и {self.edibility} и {self.hp} и {self.speed}')



#x = Creature()
#x.get_param()
