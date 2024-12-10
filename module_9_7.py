# Напишите 2 функции:

# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
# Пример:

# result = sum_three(2, 3, 6)

# print(result)



# Результат консоли:

# Простое

# 11


# Примечания:

# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three

def is_prime(func):
    def wrapper(a,b,c):
        dec=func(a,b,c) 
        if dec>1:
            for i in range(2,dec):
                if dec % i==0:
                    print('Составное') 
                    break
            print('Простое')
        else:
            print('Простое')
        return dec
    return wrapper
@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(2, 3, 6)

print(result)
