import os


print(os.path.exists('test'))  # Существует ли такая директория
print(os.name)
os.chdir('C:\\Users\Dima\Downloads')  # смена текущей директории
os.mkdir('test')  #- создает новую дирректорию
#os.rename('test', 'test3')           # Смена имени директории os.replace - с принудительной заменой


#os.rmdir('test3') - удаляет пустую директорию

"""
os.removedirs(path) - удаляет директорию, затем пытается удалить родительские директории,
 и удаляет их рекурсивно, пока они пусты.

"""

"""
os.walk(top, topdown=True, onerror=None, followlinks=False) - генерация имён файлов в дереве каталогов,
 сверху вниз (если topdown равен True), либо снизу вверх (если False). Для каждого каталога функция walk возвращает
  кортеж (путь к каталогу, список каталогов, список файлов).
"""

"""
os.system(command) - исполняет системную команду, возвращает код её завершения (в случае успеха 0).
"""