"""
Наследование классов.

PositiveList наследует класс list, метод append сохраняет функциональность родительского класса, но с условием if.
Если условие не выполняется - вызывается исключение, полностью наследованное от класса Exception.

"""
class PositiveList (list):
    def append(self, x):
        if x > 0 and int(x) == float(x):
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError


class NonPositiveError(Exception):
    pass


# пример работы:
a = PositiveList()
a.append(-1)
print(a)


