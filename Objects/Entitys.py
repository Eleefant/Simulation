#Прописываем импорт модуля с иконками например from icons import icons

class Entity:
    #picture = [] #здесь ссылка на список с картинками/иконками
    #coordinate = [] #здесь ссылка на координаты появления объекта
    #edibility = 0 не съедобен = 1 съедобен для травоядных, 2 съедобен для хищников
    def __init__(self, picture='_', edibility=0):
        self.picture = picture
        self.edibility = edibility


class Grass(Entity):
    def __init__(self):
        super().__init__('G', 1)


class Rock(Entity):
    def __init__(self):
        super().__init__('R')

    #def get_param(self):
    #    print(f'параметры травы {self.picture} и {self.edibility}')

class Tree(Entity):
    def __init__(self):
        super().__init__('T')


#x = Rock()
#x.get_param()

#print(x.__dict__)






