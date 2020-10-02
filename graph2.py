import json
from more_itertools import unique_everseen

"Обход графов. js - данные в формате JSON"

js = '[{"name": "G", "parents": ["F"]},' \
      ' {"name": "A", "parents": []},' \
      ' {"name": "B", "parents": ["A"]},' \
      ' {"name": "C", "parents": ["A"]},' \
      ' {"name": "D", "parents": ["B", "C"]},' \
      ' {"name": "E", "parents": ["D"]},' \
      ' {"name": "F", "parents": ["D"]},' \
      ' {"name": "X", "parents": []},' \
      ' {"name": "Y", "parents": ["X", "A"]},' \
      ' {"name": "Z", "parents": ["X"]},' \
      ' {"name": "V", "parents": ["Z", "Y"]},' \
      ' {"name": "W", "parents": ["V"]}]'

pyto = json.loads(js)

"""
Преобразование данных в список, содержащий словари.
"""

lst = []
for c in pyto:
    c['count'] = 0
    c['child'] = []

"""
Добавление в словари ключей - счетчик потомков и их множество (сначала это просто список)
"""


def fix(pyto, name):
    print('Find', name)
    for i in pyto:
        print('in', i['name'])
        if name in i['parents']:
            print(name, '+1 !!!! in ', i['name'])
            j['child'].append(i['name'])
            fix(pyto, i['name'])
        else:
            continue


"""
Ф-я принимает список со словарями и имя родителя для поиска. При нахождении родителя в
'parents' - класс добавляется в 'child'
"""

for j in pyto:
    print()
    fix(pyto, j['name'])

"""Страрт ф-и для каждого имени"""

for c in pyto:
    c['child'] = set(c['child'])
    c['count'] = len(set(c['child'])) + 1

"""Убрать повторы в 'child', и посчитать кол-во 'child' в 'count'"""

for rez in pyto:
    print(rez)

for i in pyto:
    lst.append(i['name'] + ' : ' + str(i['count']))

lst = set(lst)
lst = sorted(lst)

for i in lst:
    print(i)