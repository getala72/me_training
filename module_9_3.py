

# Дано 2 списка:

first = ['Strings', 'Student', 'Computers']

second = ['Строка', 'Урбан', 'Компьютер']

# Необходимо создать 2 генераторных сборки:

# В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second, если их длины не равны.  
# Для перебора строк попарно из двух списков используйте функцию zip.
# В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second. 
# Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

# first_result=(len(i)-len(g) for i,g in zip(first,second) if len (i)!= len(g))
# print(list(first_result))

join_list= zip(first,second)

first_result=(len(i[0])-len(i[1]) for i in join_list if len (i[0])!= len(i[1]))

second_result=(len(first[i])==len(second[i]) for i in range(len(first)))
# Пример результата выполнения программы:



# Пример выполнения кода:

print(list(first_result))

print(list(second_result))

# Вывод в консоль:

# [1, 2]

# [False, False, True]

# Примечания:

# Это небольшая практика, поэтому важность выполнения каждого условия обязательна.
