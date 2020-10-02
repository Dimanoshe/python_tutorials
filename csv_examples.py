import csv

"""
для изоляции значения с запятой, переносом строки и тп, например 5,43 - "5,43"

tcv - для чтения элементов, разделенных TAB

Для записи:

    
with open("temporary/Crimes.csv") as f:
    writer = csv.reader(f)
    for row in reader:   # для каждой строки документа записываем одну строку
        writer.writerow(list)
        
    для csv.reader(f) есть атрибут csv.reader(f, QUOTE)
    
QUOTE_All - все в ковычки
QUOTE_NONNUMEERIC - в ковычки все что не числовое
"""


with open("temporary/Crimes.csv") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)