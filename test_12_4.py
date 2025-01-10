
# Задача "Логирование бегунов":

# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
import unittest
import logging
import traceback
logging.basicConfig(level=logging.INFO,filename='runner_tests.log',filemode=('w'),encoding='utf-8',format='%(asctime)s | %(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

# t = Tournament(101, first, second)
# print(t.start())

# Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.



# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.

class RunnerTest(unittest.TestCase):
    is_frozen=False
    @unittest.skipIf(is_frozen is True,'Тесты в этом кейсе заморожены')  
  
    def test_walk(self):
        try:
            ron=Runner('Андрей',-5)
            for i in range(10):
               ron.walk()
            self.assertEqual(ron.distance,50)
            logging.info('"test_walk" выполнен успешно')

        except ValueError as var:
            logging.warning(msg="Неверная скорость для Runner",exc_info=True) 
    @unittest.skipIf(is_frozen is True,'Тесты в этом кейсе заморожены')    
    def test_run(self):
        try:
            ron2=Runner(22,5)
            for i in range(10):
                ron2.run
            self.assertEqual(ron2.distance,100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as te:
            logging.warning(msg="Неверный тип данных для объекта Runner",exc_info=True) 

    # def test_challenge(self):
        
    #     ob_3=Runner('ob_3')
    #     ob_4=Runner('ob_4')
    #     for i in range(10):
    #            ob_3.walk()
    #     for i in range(10):
    #             ob_4.run()      
        
    #     self.assertNotEqual(ob_3.distance,ob_4.distance)
        
if __name__=='__main__':
    unittest.main()
    

# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:




# Уровень - INFO
# Режим - запись с заменой('w')
# Название файла - runner_tests.log
# Кодировка - UTF-8
# Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.


# Дополните методы тестирования в классе RunnerTest следующим образом:

# test_walk:

# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте отрицательное значение в speed.
# В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
# test_run:

# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте что-то кроме строки в name.
# В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
# Пример результата выполнения программы:

# Пример полученного файла логов runner_tests.log: