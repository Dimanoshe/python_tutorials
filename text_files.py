"""
Режим	Обозначение
'r'	открытие на чтение (является значением по умолчанию).
'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
'x'	открытие на запись, если файла не существует, иначе исключение.
'a'	открытие на дозапись, информация добавляется в конец файла.
'b'	открытие в двоичном режиме.
't'	открытие в текстовом режиме (является значением по умолчанию).
'+'	открытие на чтение и запись
"""

"""
ЧТЕНИЕ
"""

with open('temporary/test.txt', "r") as f:   # атрибут "r" не обязателен, тк вкл по умолчанию
    x = f.read(68)                   # Вывод первых 100 символов, при f.reed() - в x записываются все данные
    print(x)
    print()
    print(repr(x))                   # Вывод в формате строки
    print()
    print(x.splitlines())            # В формате списка по строкам или по пробелам
    print(repr(x).rsplit())

print()
print()
"""
Пример итерации для экономии памяти и быстродействия:
"""

with open('temporary/test.txt') as f:
    for line in f:
        line = line.rstrip()          # работа метода .rstrip() - убирает лишнее справа
        print(repr(line))
    x = f.read()
    print(repr(x))                    # возврат пустой строки, т.к. больше нечего вывести


"""
ЗАПИСЬ
"""
some_list = ['\n1 строка', '2 строка', '3 строка']
with open('temporary/in.txt', "a") as f:
    f.write("NAME\nTest file1\n\nText.")
    """
    Создание файла в указанной директории с указанным текстом, если файл с таким именем уже был, его содержимое 
    изменится на указанное.
    """
    cont = '\n'.join(some_list)
    f.write(cont)
    """
    Запись в файл из списка. Используется метод приобразования из списка в строку,
     'чем разделять'.join(список)
    """
