"""
Задача на вывод значений из списка, соответствующих одному или нескольким условиям
аналог класса filter

"""



class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True   # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        else:
            return False

    def judge_any(pos, neg):
        if pos >= 1:
            return True   # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        else:
            return False

    def judge_all(pos, neg):
        if neg == 0:
            return True   # допускает элемент, если его допускают все функции (neg == 0)
        else:
            return False

    """
    Допускающие ф-ии, сравнивают веса, сгенерированные на основании фильтрующих ф-ий, в данном примере максимальное
    значение pos и neg равно 3 (т.к. 3 фильтрующие функции) 
    """

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # исходная последовательность
        self.funcs = funcs  #допускающие функции
        self.judge = judge  #решающая функция

    """
    Конструктор класса, задающий объекту(последовательность, проверяющие(фильтрующие) функции, допускающая ф-я)
    """

    def __iter__(self):
        for i in self.iterable:              # проход по последовательности
            self.neg = 0                     # обнуление весов перед новым сравнением
            self.pos = 0
            for j in self.funcs:             # проход по проверяющим ф-ям
                if j(i) == True:
                    self.pos += 1
                else:
                    self.neg += 1
            print(i, '   ', self.pos, ' ', self.neg, ' ', self.judge(self.pos, self.neg))

            if self.judge(self.pos, self.neg) == True:
                yield i                      # вывод значения при выполнении условий


def mul2(x):                            # фильтрующие функции в произвольном кол-ве (>1) выдают True или False
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # генератор проверяемого списка списка

print(list(multifilter(a, mul2, mul3, mul5)))
