"""Пример работы итератора:


book = {'a': 12, 'b': 123, 'er': 46, 'io': 111}
iterator = iter(book)  # Кроме словаря можно использовать списки, множества и строки

while True:
    try:
        x = next(iterator)  # При первом вызове next - 0 значение, и так до исключения StopIteration
        print(x)
    except StopIteration:   # 'for i in book:' - аналог приведенногго цикла
        break

print()

"""

from random import random


class RandInt:  # Создание класса
    def __iter__(self):  # Определение метода
        return self

    def __init__(self, k):   # конструктор, где k кол-во итерируемых элементов
        self.k = k
        self.i = 0           # Счетчик

    def __next__(self):      # Функция с простым условием выведения случайного числа
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration  # Вызов исключения


"""
Если не определять класс RandInt, то:
for i in range(5):
    print(random())
"""

for i in RandInt(5):
    print(i)

print()


"""
Еще один пример собственного итератора:
особенность заключается в том, что метод next выводит итерируемые элементы парами, в случае если кол-во эл-тов нечетное
вызывается исключение list index out of range.
StopIteration вызывается, как обычно.
"""
print()

class DublIter:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i +=2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


class Mylist(list):
    def __iter__(self):
        return DublIter(self)


"""
Класс Mylist полностью наследует класс list, за исключением метода __iter__, который в данном случае выводит результат 
объекта класса DublIter.
"""
for i in Mylist([1, 2, 3, 4]):
    print(i)

"""
Пример работы генератора:
Особенность работы генератора в том, что в отличии от циклов здесь не создаются списки. Повторный вызов такой ф-ии не 
начинает цикл заново, а сразу выдает следующее значение.    
"""


def rand_gen(k):           # ф-я принимает 1 аргумент - кол-во итерируемых объектов.
    for j in range(k):
        yield random()


x = rand_gen(3)
for i in x:
    print(i)

print()

"""
Еще один пример создания генератора списков (list comprehension)
Список[] и генератор()
"""



gen = [(x, y) for x in range(3) for y in range(3) if y >= x]  # Подходит для подбора значения!
gen1 = [(x, y, z) for x in range(3) for y in range(3) for z in range(4)]
print(gen)
print(gen1)
print()

gen3 = ((x, y) for x in range(3) for y in range(3) if y >= x)
print(next(gen3))
print(next(gen3))