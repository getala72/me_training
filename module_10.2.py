# Задача "За честь и отвагу!":
import time
from threading import Thread

# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
class Knight(Thread):
     def __init__(self,name,power):
          super().__init__()
          self.name=name
          self.power=power
          self.enemy=100
          self.days=0

     def run(self):
          print(f"{self.name}, на нас напали!")
          while self.enemy>0:
                time.sleep(1)
                self.days+=1
                self.enemy-=self.power
                if self.enemy<0:
                    self.enemy=0
                print(f"{self.name} сражается {self.days}..., осталось {self.enemy} воинов.") 
          print(f"{self.name} одержал победу спустя {self.days} дней(дня)!") 


             



# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:

# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.

# Пункты задачи:

# Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight.
# Выведите на экран строку об окончании битв.


# Пример результата выполнения программы:

# Алгоритм выполнения кода:

# # Создание класса

first_knight = Knight('Sir Lancelot', 10)

second_knight = Knight("Sir Galahad", 20)

first_knight.start()

second_knight.start()

first_knight.join()

second_knight.join()

print('Все битвы закончились!')









# # Запуск потоков и остановка текущего

# # Вывод строки об окончании сражения

# Вывод на консоль:

# Sir Lancelot, на нас напали!

# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.

# Sir Galahad, на нас напали!

# Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.

# Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.

# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.

# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.

# Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.

# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.

# Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.

# Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.

# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.

# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.

# Sir Galahad одержал победу спустя 5 дней(дня)!

# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.

# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.

# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.

# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.

# Sir Lancelot одержал победу спустя 10 дней(дня)!

# Все битвы закончились!


