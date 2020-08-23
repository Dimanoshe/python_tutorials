"""
Решение задачи по нахождению лишних исключений (обход графов).
Пример входных данных:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Выход:

FileNotFoundError
"""

from more_itertools import unique_everseen

"""Импорт модуля для создания списка с уникальными значениями без изменения порядка"""

n = int(input())
cls_exp = [str(input()) for i in range(n)]
m = int(input())
exp = [str(input()) for j in range(m)]
dct_cls_exp = {}
print_list = []
while_count = 0

"""
n, m - кол-во строк в списках: cls_exp - дерево наследников, exp - последовательность исключений.
dct_cls_exp - пусто словарь для дерева наследников, print_list - список для вывода ответа (лишние исключения).
while_count - счетчик
"""


for i in cls_exp:
    i = i.split(' : ')
    if len(i) == 2:
        dct_cls_exp[i[0]] = i[1]
    else:
        dct_cls_exp[i[0]] = 'None'

"""
Создание словаря с указанием родителей. Если родитель не указан - присваевается значение 'None'.
В противном случае - один или несколько родителей в строке.
"""


def check(from_exp_parrent, excep, while_count):
    print(while_count)
    for j in excep:
        for g in from_exp_parrent.split():
            print("Сравниваем", g, "и", j)
            if while_count == len(exp):
                return
            while_count += 1
            if g == j:
                print_list.append(i)
                print('Найден!', i, 'по родителю -', g)
                return
            if while_count == len(exp):
                return
            elif from_exp_parrent == 'None':
                return
            else:
                check(dct_cls_exp[g], exp[:exp.index(i)], while_count)

    """
Функция проверки (родитель, часть списка до проверяемого исключения, счетчик (максимальное значение - 
кол-во исключений))
1. Проход по списку до проверяемого исключения.
2. Сравнениеродителя(лей) и предыдущих исключений
3. Если совпадение есть то исключение записывается в список вывода ответа, иначе функция испалняется еще раз с проверкой
 следующего родителя.

    """


for i in exp:
    print('Проверяется', i)
    if exp.index(i) == 0:
        pass
    if exp.index(i) == len(exp):
        break
    else:
        check(dct_cls_exp[i], exp[:exp.index(i)], while_count)

for i in unique_everseen(print_list):
    print(i)


"""
Тестовый пример: 
14
a
b : a
c : a
f : a
d : c b
g : d f
i : g
m : i
n : i
z : i
e : m n
y : z
x : z
w : e y x
9
y
m
n
m
d
e
g
a
f
"""
