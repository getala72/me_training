# Дополнительное практическое задание по модулю: "Наследование классов."


# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности


# Задание "Они все так похожи":

# 2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.

# Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?

# Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного использования таких объектов?


# По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон, цвет и др.


# Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):


# Общее ТЗ:

# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.

# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.


# Подробное ТЗ:

import math
# Атрибуты класса Figure: sides_count = 0
class Figure:
    def __init__(self):
       self.sides_count = 0
       self.__sides=0
       self.__color=(0,0,0)
       self.filled=True


    def get_color(self):
        return list(self.__color)


    def __is_valid_color(self,new_color):
        is_valid_color = True if len(new_color)  == 3 else False
        if not is_valid_color:
           return is_valid_color
        for i in new_color:
            is_valid_color=True if i in range(256) and type(i)==int else False
            if not is_valid_color:
                break
        return is_valid_color  
    


    def set_color(self,*new_color):
        if type(new_color[0])==tuple:new_color=new_color[0]
        if self.__is_valid_color(new_color):
            self.__color=new_color
        # else:
        #     print(f"Такого цвета {new_color} не существует")



    def __is_valid_sides(self,new_sides):
        is_valid_sides = True if len(new_sides)  == self.sides_count else False
        if not is_valid_sides:
           return is_valid_sides
        for i in new_sides:
            is_valid_sides=True if type(i)==int and i > 0 else False
            if not is_valid_sides:
                break
        return is_valid_sides 
    
    def set_sides(self,*new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], (list, tuple)):
            new_sides = new_sides[0]
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
        #else:
            #print("Некорректные параметры ввода")

    def get_sides(self):
        return list(self.__sides)
    

    def  __len__(self):
        return sum(self.__sides)
    
    
class Circle(Figure):
    def __init__(self,color_,*new_sides):
        super().__init__()
        self.sides_count = 1
        super().set_color(color_)
        super().set_sides(self.__sides__circle(new_sides))
        self.set_radius()
    def __sides__circle(self,new_sides):
        if len(new_sides)!=self.sides_count:
            new_sides=[]
            new_sides.append(1)
            new_sides=tuple(new_sides)
            return new_sides
        return new_sides

        
    def set_radius(self):
        self.__radius=super().__len__()/2/math.pi
        return
    def get_radius(self):
        return self.__radius
    def get_square(self):
        return math.pi*self.get_radius()**2

class Triangle(Figure):
    def __init__(self,color_,*new_sides):
        super().__init__()
        self.sides_count = 3
        super().set_color(color_)
        super().set_sides(self.__sides_triangle(new_sides))
        
    def __sides_triangle(new_sides):
        if len(new_sides)!=self.sides_count:
            new_sides=[]
            for _ in range(self.sides_count):new_sides.append(1)
            new_sides=tuple(new_sides)
        return new_sides
    def get_square(self):
        s=super().__len__()/2
        for i in super().get_sides():
            s*=super().__len__()/2-i
        return math.sqrt(s)  

class Cube(Figure):  
    def __init__(self,color_,*new_sides):
        super().__init__()
        self.sides_count = 12
        super().set_color(color_)
        super().set_sides(self.__sides_cube(new_sides))
        
    def __sides_cube(self,new_sides):
        new_2_sides= 1 if len(new_sides)!=1 else list(new_sides)[0]
        new_sides=[]
        for i  in range(self.sides_count):new_sides.append(new_2_sides)
        new_sides=tuple(new_sides)
        return new_sides
    
    def get_volume(self):
        self.__sides=super().get_sides()
        return list(self.__sides)[0]**3

           

# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.


# ВАЖНО!

# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.

# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]

# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]

# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)

# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]



# Код для проверки:

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

print(cube1.get_color())



# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())


# Проверка периметра (круга), это и есть длина:

print(len(circle1))


# Проверка объёма (куба):

print(cube1.get_volume())


# Выходные данные (консоль):

# [55, 66, 77]

# [222, 35, 130]

# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

# [15]

# 15

# 216


# Примечания (рекомендации):

# Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
# Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
# Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
# Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
# Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!