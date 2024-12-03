# Задача:

# Даны несколько списков, состоящих из строк


first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result=[len(i) for i in first_strings if len(i)>5]

second_result=[(i,g) for i in first_strings for g in second_strings if len(i)==len(g)]

third_result={i:len(i) for i in first_strings+second_strings if len (i) %2==0}


# for i in first_strings:
#     if len(i)>5:
#         first_result.append(len(i))


# for i in first_strings:
#     for g in second_strings:
#         if len(i)==len(g):
#             second_result.append((i,g))

# for i in first_strings+second_strings:
#     if len (i) %2==0:
#         third_result[i]=len(i)


print(first_result)
print(second_result)
print(third_result)
        




# В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
# В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. 
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
# В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки. 
# Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.

# Пример результата выполнения программы:

# Пример выполнения кода:

# print(first_result)

# print(second_result)

# print(third_result)

# Вывод на консоль:

# [10, 8, 8]

# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]

# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}



# Примечания:

# Помните, когда вы используете 2 цикла for внутри сборки, первый цикл - внешний, второй - внутренний.