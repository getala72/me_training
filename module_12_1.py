# Задача "Проверка на выносливость":

# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)

# В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

# class Runner:
#     def __init__(self, name):
#         self.name = name
#         self.distance = 0

#     def run(self):
#         self.distance += 10

#     def walk(self):
#         self.distance += 5

#     def __str__(self):
#         return self.name

# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:

# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. 
# После чего методом assertEqual сравните distance этого объекта со значением 50.
# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual 
# сравните distance этого объекта со значением 100.
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. 
# Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.


import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_fro=False

    def walk_ob(self,ob):
        for i in range(10):
            ob.walk()

    def run_ob(self,ob):
        for i in range(10):
            ob.run()

    @unittest.skipIf(is_fro is True,'Тесты не доступны')  
    def test_walk(self):
        ob_1=runner.Runner('ob_1')
        self.walk_ob(ob_1)
        self.assertEqual(ob_1.distance,50)

    @unittest.skipIf(is_fro is True,'Тесты не доступны')  
    def test_run(self):
        ob_2=runner.Runner('ob_2')
        self.run_ob(ob_2)
        self.assertEqual(ob_2.distance,100)
    @unittest.skipIf(is_fro is True,'Тесты не доступны')
    def test_challenge(self):
        ob_3=runner.Runner('ob_3')
        ob_4=runner.Runner('ob_4')
        self.walk_ob(ob_3)
        self.walk_ob(ob_3)
        self.run_ob(ob_4)
        self.run_ob(ob_4)
        self.assertNotEqual(ob_3.distance,ob_4.distance)
        


if __name__=='__main__':
    unittest.main()
   

# Пункты задачи:

# Скачайте исходный код для тестов.
# Создайте класс RunnerTest и соответствующие описанию методы.
# Запустите RunnerTest и убедитесь в правильности результатов.
# Пример результата выполнения программы:

# Вывод на консоль:

# Ran 3 tests in 0.001s OK



# Примечания:

# Попробуйте поменять значения в одном из тестов, результаты

