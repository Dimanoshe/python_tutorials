import os
from more_itertools import unique_everseen

"""
unique_everseen - для уникальных значений без изменения последовательности.

1. переход в рабочую директорию
2. os.walk(top='main') - рекурсивная генерация файлов в папках, где tree - кортедж, в котором каждый элемент имеет
следующую структуру: i(0) - название директории, i(1) - вложенные директории, i(2) -  файлы
"""

os.chdir('C:\\Users\Dima\Downloads')

#print(os.path.exists('sample'))

out = []

tree = os.walk(top='main')
for i in tree:
    #print(i)
    for j in i[2]:
        if j[-3:] == '.py':
            #print('!!!')
            #print(i[0])
            out.append(i[0])
            #print('!!!')

print('\n'.join(list(unique_everseen(out))))

"""
Программа определяет в каких директориях есть файлы .py и выводит их в формате строки, разделенной \n
"""

