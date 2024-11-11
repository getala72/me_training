# Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.

class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,owner,model,color, engine_power):
        self.owner=owner
        self.__model=model
        self.__engine_power=engine_power
        self.__color=color


    def get_model(self):
        return f"Модель: {self.__model}"
    
    def get_horsepower(self): 
        return f"Мощность двигателя: {self.__engine_power}"
    
    def get_color(self): 
       return f"Цвет: {self.__color}"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")
    def set_color(self,new_color):
        if new_color.lower() in [i.lower() for i in self.__COLOR_VARIANTS]:
            self.__color=new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")
            

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self,owner,model,color, engine_power):
        super().__init__(owner,model,color, engine_power)




# Пункты задачи:

# Создайте классы Vehicle и Sedan.
# Напишите соответствующие свойства в обоих классах.
# Не забудьте сделать Sedan наследником класса Vehicle.
# Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.


# Пример результата выполнения программы:

# Исходный код:

# # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)



# Изначальные свойства

vehicle1.print_info()



# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'



# Проверяем что поменялось

vehicle1.print_info()

