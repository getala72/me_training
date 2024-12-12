# Задача "Потоковая запись в файлы":

# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.

# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.

# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.

# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
from time import sleep
from threading import Thread
from datetime import datetime

def wite_words(word_count, file_name):
    with open(file_name,'w',encoding='utf-8') as f:
        for i in range(1,word_count+1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}" )
timestart=datetime.now()



# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:

wite_words (10, 'example1.txt')
wite_words (30, 'example2.txt')
wite_words (200,'example3.txt')
wite_words (100,'example4.txt')
timeand=datetime.now()
timeres=timeand-timestart
print(f'работа потоков {timeres}')

timestart_th=datetime.now()
first=Thread(target=wite_words,args=(10, 'example5.txt'))
second=Thread(target=wite_words,args=(10, 'example6.txt'))
tree=Thread(target=wite_words,args=(10, 'example7.txt'))
four=Thread(target=wite_words,args=(10, 'example8.txt'))

first.start()
second.start()
tree.start()
four.start()


first.join()
second.join()
tree.join()
four.join()

timeand_th=datetime.now()
timeres_th=timeand_th-timestart_th
print(f'работа потоков {timeres_th}')






# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:

# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.

# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.



# Пример результата выполнения программы:

# Алгоритм работы кода:

# # Импорты необходимых модулей и функций

# # Объявление функции write_words

# # Взятие текущего времени

# # Запуск функций с аргументами из задачи

# # Взятие текущего времени

# # Вывод разницы начала и конца работы функций

# # Взятие текущего времени

# # Создание и запуск потоков с аргументами из задачи

# # Взятие текущего времени

# # Вывод разницы начала и конца работы потоков

# Вывод на консоль:

# Завершилась запись в файл example1.txt

# Завершилась запись в файл example2.txt

# Завершилась запись в файл example3.txt

# Завершилась запись в файл example4.txt

# Работа потоков 0:00:34.003411 # Может быть другое время

# Завершилась запись в файл example5.txt

# Завершилась запись в файл example6.txt

# Завершилась запись в файл example8.txt

# Завершилась запись в файл example7.txt

# Работа потоков 0:00:20.071575 # Может быть другое время



# Записанные данные в файл должны выглядеть так:



# Примечания:

# Не переживайте, если программа выполняется долго, учитывая кол-во слов, максимальное время выполнения в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
# Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt, т.к. потоки работали почти одновременно.

