# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

# Задача:

# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться 
# подпоследовательности переданной строки.

# Пункты задачи:

# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.
# Пример результата выполнения программы:

# Пример работы функции:

# a = all_variants("abc")

# for i in a:

# print(i)

# Вывод на консоль:

# a

# b

# c

# ab

# bc

# abc


# Примечания:

# Для функции генератора используйте оператор yield.


# def all_variants(text):
#     for i in range(len(text)+1):
#         for r in range(i):
#             if r < len(text):
#                 yield text[r:i]

        
# a = all_variants("abc")
# for i in a:

#     print(i)  

def all_variants(text):
    for i in range(1,len(text)+1):
        for r in range(len(text)-i+1):
            yield text[r:r+i]
              
a = all_variants("abc")
for i in a:

    print(i)  



