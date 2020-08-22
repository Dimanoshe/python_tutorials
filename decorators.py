def decor(fun):
    # ф-я декоратора
    def decact():
        print("Я - код, который отработает до вызова функции")
        fun()
        print("А я - код, срабатывающий после")
    # то,  что происходит
    return decact


def decor2(fun):
    # еще одна ф-я декоратора
    def decact():
        print('*************************')
        fun()
        print('=========================')
    return decact


def testfun():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
    # декорируемая функция


new_fun = decor(testfun)
new_fun()
# Перезапись и вызов ф-ии
print()


@decor2
@decor
def testfun2():
    print('Вторая ф-я прошла')
# Использование декораторов для любых ф-й


testfun2()

print()


def decor3(fun):
    # ф-я декоратора c аргументами
    def decact(arg1, arg2):
        print("Смотри, что я получил:", arg1, arg2)
        fun(arg1, arg2)
    return decact



@decor3
def eat(eat1, eat2):
    print("Теперь у меня есть", eat1, eat2)
# Использование декораторов с аргументами


eat('Kola', 'chips')

