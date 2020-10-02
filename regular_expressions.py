import requests as req
import re


pattern = r'a[rctb\?]c'  # шаблон, где 2 символ может быть r, t ИЛИ b. "?" - один из метасимволов, "\" - его экран.
"""
В шаблоне можно указать диапазон циыр или букв: [3-9] или [a-z] или [a-zA-Z]

\d - [0-9] (цифры)
\D - [^0-9] (все, кроме цифр)
\s - [\t\r\n\f\v] (пробельные символы)
\S - [^\t\r\n\f\v] (все, кроме пробельных)
\w - цифробуквенные последовательности + _
\W - все кроме w
.  - все символы

b* - любое кол-во b, даже 0
b+ - любое колво b от 1 и >
b? - 0 или 1 вхождение b
b{3} - 3b в строке
b{2-6} - от 2 до 6 вхождений b
adsc|brtg - adsc или brtg
b\b - после b нет ни цифр ни букв  \bb - передb нет ни цифр ни букв

"""


string = 'ewabcdsfdsabcd'   # то, где будем искать

match_obj = re.search(pattern, string)  # (что ищем, где ищем)

"""
Возвращает <re.Match object; span=(0, 3), match='abc'>, где span - интервал где нашли (первое вхождение),
 math - что нашли.
 
 https://regex101.com - онлайн отладка
 
"""

print(match_obj)

print()

string2 = 'abc, acc, atc'
all_inclusions = re.findall(pattern, string2)  # находим все вхождения согласно шаблону
print(all_inclusions)

fix = re.sub(pattern, 'ooo', string2)  # исправили все, найденое в строке по шаблону на 'ooo'
print(fix)

x = re.match(r'text', 'TEXT', re.IGNORECASE)  # использование флага (заглавнеые и прописные)
print(x)


"""
Примеры


pattern = r'\b(\w+)(\1)\b'  # Слово состоящее из 2ух одинаковых половинок
find = re.findall(pattern, line)  # Вывод таких слов

pattern = r'\b(\w)(\w)(\w*)\b'  # Найти все слова, состоящие из букв и выделить в отдельные группы 2 первых буквы
find = re.sub(pattern, r'\2\1\3', line) # вывод с указанием последовательности групп 

pattern = r'((\w)\2+)'  # ищем группы повторяющихся букв
find = re.sub(pattern, r'\2', line) # заменяем на 2 группу (тк вторые открывающиеся скобки)

Задача.
Вывести все адреса со страницы, используя Regular exception
"""

lst = []
link_file = "http://pastebin.com/raw/7543p0ns"

open_file = req.get(link_file)


pattern = r"(?:<[alink] .*href=)(?:['|\"]\w+:\/\/)?(\w[0-9a-zA-Z.-]+)?(?:[\"|'](?:[0-9a-zA-Z.-]+.*w{2,3}(?:\"|')))?"

find = re.findall(pattern, open_file.text)


for i in find:
    if len(i) >= 6:
        lst.append(i)

lst = set(lst)
lst = sorted(lst)

print(len(lst))

for i in lst:
    print(i)