"""
Генератор простых чисел по теореме Вильсона.


"""


def primes():                         # Ф-я на определение простого числа
    a = 2
    print('computation for ', a)
    while True:
        if (factorial(a - 1) + 1) % a == 0:
            yield a                   # вывод следующего натурального числа, если оно простое
        a += 1


def factorial(f):                     # Вычисление факториала
    n = 1
    for i in range(1, f + 1):
        n *= i
    return n


x = primes()


count = int(input('number of primes: '))  # кол-во простых чисел для вывода

for i in range(count):
    print(next(x))

