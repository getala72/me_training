'''Задание "Слишком древний шифр":

Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").

К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.

Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.

В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.



К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).



Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.



Пример кратности(деления без остатка):

1 + 2 = 3 (сумма пары)

9 / 3 = 3 (ровно 3 без остатка)

9 кратно 3 (9 делится на 3 без остатка)





Пример 1:

9 - число из первой вставки

1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)



Пример 2:

11 - число из первой вставки

11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)





К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движутся на вас (обожаю клише), тем более числа в первой вставке будут попадаться случайно.



Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа.



Что является парой?:

Пары являются уникальными на примере следующего:

7 3 3 5 8

Пример работы алгоритма с иллюстрацией (см. картинку):

Для первой 7: 73 73 75 78

Для второй 3: 33 35 38 (с первой 7 у этой 3 уже есть пара, поэтому её не берём).



Все пароли для чисел от 3 до 20 (для сверки):

3 - 12

4 - 13

5 - 1423

6 - 121524

7 - 162534

8 - 13172635

9 - 1218273645

10 - 141923283746

11 - 11029384756

12 - 12131511124210394857

13 - 112211310495867

14 - 1611325212343114105968

15 - 1214114232133124115106978

16 - 1317115262143531341251161079

17 - 11621531441351261171089

18 - 12151811724272163631545414513612711810

19 - 118217316415514613712811910

20 - 13141911923282183731746416515614713812911



Отдельно по числам, для большего понимания:

3 - 1+2

4 - 1+3

5 - 1+4 2+3

6 - 1+2 1+5 2+4

7 - 1+6 2+5 3+4

8 - 1+3 1+7 2+6 3+5

...

18 - 1+2 1+5 1+8 1+17 2+4 2+7 2+16 3+6 3+15 4+5 4+14 5+13 6+12 7+11 8+10

19 - 1+18 2+17 3+16 4+15 5+14 6+13 7+12 8+11 9+10

20 - 1+3 1+4 1+9 1+19 2+3 2+8 2+18 3+7 3+17 4+6 4+16 5+15 6+14 7+13 8+12 9+11

Примечания:

Можно использовать как цикл for, так и цикл while
Первое число не входит в одно из чисел пары
Пары чисел подбираются от 1 до 20 для текущего числа.




Файл с кодом (module_2_hard.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.
'''
"Вариант 1"

import random


num_list = []


def list_create(start=3,end=20):
    for i in range(start, end + 1):
        num_list.append(i)
    return num_list

def left_num():
    left = list_create()[random.randint(list_create()[0],len(list_create()))]
    return left

def spisok_par(n=20):

    spisok = []
    for i in range(n,0,-1):
        para = []
        if i >= 0 and n-i > 0:
            #print(n-i,'+',i)
            if (n-i) or i not in para:
                para.append(n-i)
                para.append(i)
            if [para[1],para[0]] not in spisok:
                spisok.append(para)

        else:
            continue
    return spisok



def algoritm(get_num):
    right_list = []

    for i in range(get_num-1,0,-1):
        if get_num % i == 0:
            if len(spisok_par(i)) > 0:
                for p in spisok_par(i):
                    right_list.append(p)
    for i in spisok_par(get_num):
        right_list.append(i)
    for i in right_list:
        if i[0] == i[1]:
            right_list.remove(i)
    right_list = sorted(right_list)
    result = ''
    for x in right_list:
        for y in x:
            result += str(y)
    print("Число слева:", get_num, "Пароль:", result)


def result():
    for i in list_create(3,20):
        algoritm(i)


result()


"Вариант 2"

from random import randint

def get_password(first_number):
    second_number = []
    list_couples = []
    for i in range(1, first_number):
        for j in range(1, first_number):
            if all([first_number % (i + j) == 0 and i != j and [j, i] not in list_couples]):
                list_couples.append([i, j])
    for i in list_couples:
        second_number.extend(i)
    password = ''.join(str(i) for i in second_number)
    return password

for random_number in range(3, 21):
    result = get_password(random_number)
    print(f'{random_number} - {result}')