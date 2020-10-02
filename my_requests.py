from bs4 import BeautifulSoup as BS
import requests as req
import re



url_1 = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html'
url_refer = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'


def check(url_1, url_refer):
    url_first_step = req.get(url_1)
    print(url_first_step)
    if str(url_first_step) != '<Response [200]>':
        return 'No'
    print('переход по первой ссылке выполнен')

    cont = BS(url_first_step.text, 'html.parser')
    #print('содержание файла:\n', cont)

    print('Проверка доступных ссылок:\n')
    for i in cont.find_all('a'):
        if len(i.get('href')) == 0:
            print('доступных ссылок нет((')
            return 'No'

        print(i.get('href'))
        try:
            check_file = req.get(i.get('href'))
            print(check_file)
            if check_file == None:
                print('пустой файл')
                
            if str(check_file) != '<Response [200]>':
                return 'No'
            print('Содержание:\n')
        except:
            print('некоректная ссылка')
            break
        for j in BS(check_file.text, 'html.parser').find_all('a'):
            if len(j.get('href')) == 0:
                return 'No'
            print(j.get('href'))
            if j.get('href') == url_refer:
                return 'Yes'
            else:
                return 'No'


if url_1 != '':

    print(check(url_1, url_refer))

else:
    print('No')

