# Задание "Программистам всё можно":

# Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем сложить число(int) и строку(str)? Давайте исправим это недоразумение!



# Реализуйте следующую функцию:

# add_everything_up, будет складывать числа(int, float) и строки(str)

# def add_everything_up(a,b):
#     try:
#         return a+b
    
#     except TypeError:
#         return f'{a}{b}'

def add_everything_up(a, b):
    try:

        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b

        elif isinstance(a, str) and isinstance(b, str):
            return a + b

        else:
            raise TypeError
    except TypeError:

        return f'{str(a)}{str(b)}'


# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))  




# Описание функции:

# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).

# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух данных вместе (в том же порядке). 
# Во всех остальных случаях выполнять стандартные действия.


# Вывод в консоль:

# 123.456строка

# яблоко4215

# 130.456



# Примечания:

# Конструкции try-except в функции выполняют строго ту обработку, которая написана в задании (обращайте на важность порядка передачи данных).
# Если хотите дополнить функции своими исключениями или написать отдельно дополнительно собственные функции - это не запрещено, мы не против, чтобы вы больше экспериментировали. Но в первую очередь выполните поставленную задачу.