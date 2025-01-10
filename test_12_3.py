# Задача "Заморозка кейсов":

# Подготовка:

# В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.

# Часть 1. TestSuit.

# Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
# Часть 2. Пропуск тестов.

# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать 
# и выводить сообщение 'Тесты в этом кейсе заморожены'.
# Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.

# Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.



# Пример результата выполнения тестов:

# Вывод на консоль:

# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok

# test_run (tests_12_3.RunnerTest.test_run) ... ok

# test_walk (tests_12_3.RunnerTest.test_walk) ... ok

# test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'

# test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'

# test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'

# ----------------------------------------------------------------------

# Ran 6 tests in 0.000s OK (skipped=3)

import runner
import unittest
import inspect
from runner_and_tournament import Tournament as rt

class TournamentTest(unittest.TestCase):
    is_frozen=True
    def setUp(self):

        self.runner1=runner.Runner('Усэйн',10)
        self.runner2=runner.Runner('Андрей',9)
        self.runner3=runner.Runner('Ник',3)
    @classmethod
    def setUpClass(cls):
        cls.all_result={}
    @classmethod
    def tearDownClass(cls):
        dict_={}
        for i in cls.all_result:
            dict_[i]=cls.all_result[i].name
        print(dict_)
    
    @unittest.skipIf(is_frozen is True,'Тесты в этом кейсе заморожены')
    def test_start1(self):
        ob=rt.Tournament(90,self.runner1,self.runner3)
        self.all_result.update(ob.start())
        self.assertTrue(self.all_result[2]==self.runner3.name)
        self.tearDownClass()
    @unittest.skipIf(is_frozen is True,'Тесты в этом кейсе заморожены')
    def test_start2(self):
        ob=rt.Tournament(90,self.runner2,self.runner3)
        self.all_result.update(ob.start())
        self.assertTrue(self.all_result[2]==self.runner3.name)
        self.tearDownClass()
    @unittest.skipIf(is_frozen is True,'Тесты в этом кейсе заморожены')
    def test_start3(self):
        ob=rt.Tournament(90,self.runner1,self.runner2,self.runner3)
        self.all_result.update(ob.start())
        self.assertTrue(self.all_result[3]==self.runner3.name)
       

class RunnerTest(unittest.TestCase):
    is_frozen=False

    def walk_ob(self,ob):
        for i in range(10):
            ob.walk()

    def run_ob(self,ob):
        for i in range(10):
            ob.run()

    @unittest.skipIf(is_frozen is True,'Тесты в этом кейсе заморожены')  
    def test_walk(self):
        ob_1=runner.Runner('ob_1')
        self.walk_ob(ob_1)
        self.assertEqual(ob_1.distance,50)

    @unittest.skipIf(is_frozen is True,'Тесты в этом кейсе заморожены')  
    def test_run(self):
        ob_2=runner.Runner('ob_2')
        self.run_ob(ob_2)
        self.assertEqual(ob_2.distance,100)
    @unittest.skipIf(is_frozen is True,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        ob_3=runner.Runner('ob_3')
        ob_4=runner.Runner('ob_4')
        self.walk_ob(ob_3)
        self.walk_ob(ob_3)
        self.run_ob(ob_4)
        self.run_ob(ob_4)
        self.assertNotEqual(ob_3.distance,ob_4.distance)
        


test_up=unittest.TestSuite()
test_up.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_up.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runn=unittest.TextTestRunner(verbosity=2)
runn.run(test_up)

