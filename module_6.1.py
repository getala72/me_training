# Цель: применить базовые знания о наследовании классов для решения задачи



# Задача "Съедобное, несъедобное":

# Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды... Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?



# Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.



# Создайте:

# 2 класса родителя: Animal, Plant

class Animal:
    def __init__(self, name ):
        self.name=name
        self.alive = True
        self.fed = False
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed=True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive=False


# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.

# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
class Mammal(Animal):
    def __init__(self,name):
        super().__init__(name)

class Predator(Animal):
    def __init__(self,name):
        super().__init__(name)

     

# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.

# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

class Plant:
    def __init__(self, name ):
        self.name=name
        self.edible = False
    def eat(self, animal):
        animal.eat(self)

class Flower(Plant):
    def __init__(self,name):
        super().__init__(name)
        
        

class Fruit(Plant):
    def __init__(self,name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)



print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# # Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

# Вывод на консоль:
# Волк с Уолл-Стрит

# Цветик семицветик

# True

# False

# Волк с Уолл-Стрит не стал есть Цветик семицветик

# Хатико съел Заводной апельсин

# False

# True


# Примечания:

# Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
# Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться к их атрибутам внутри.
# Обращайте внимание на то, где атрибут класса, а где атрибут объекта.
# Файл module_6_1.py и загрузите его на ваш GitHub репозиторий и пришлите ссылку на него.'''


