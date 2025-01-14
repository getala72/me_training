# Цель задания:

# Закрепить знания об интроспекции в Python.

# Создать персональную функции для подробной интроспекции объекта.

# Задание:

import inspect
from pprint import pprint


class Class1():
    at = 1
    
def  introspection_info(obj):
    info=dict()
    info['type']=type(obj).__name__
    info['methods']=[i[0] for i in inspect.getmembers(obj) if 'method' in str(i[1])] 
    info['attributes']=[i for i in dir(obj) if i not in info['methods']]
    info['module']=inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None
    info['doc']=inspect.getdoc(obj)
    return info
 
 
   

# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы,
#  модуль, и другие свойства.

# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.

# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.

# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:

#   - Тип объекта.

#   - Атрибуты объекта.

#   - Методы объекта.

#   - Модуль, к которому объект принадлежит.

#   - Другие интересные свойства объекта, учитывая его тип (по желанию).

# Пример работы:
if __name__=='__main__':

 number_info = introspection_info(42)

 print(number_info)

# Вывод на консоль:

# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}

# Рекомендуется создавать свой класс и объект для лучшего понимания

# Файл с кодом прикрепите к домашнему заданию.