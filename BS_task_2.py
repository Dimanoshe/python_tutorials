from bs4 import BeautifulSoup as BS
import requests as req
import lxml

url_1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
url_refer = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
lst = []
lst_fin = []
def check(url_1, url_refer):
    go_url_1 = req.get(url_1)
    print('resp = ', go_url_1)
    if str(go_url_1) != '<Response [200]>':
        return 'No'
    print('переход по первой ссылке выполнен')

    cont = BS(go_url_1.text, 'lxml')
    # print('содержание файла:\n', cont)
    print('Проверка доступных ссылок:\n')
    for i in cont.find_all('a'):
        i = i.get('href')

        try:
            i = req.get(i)
        except:
            return
        if len(i.text) >= 0 and i.text != None:
            find = BS(i.text, 'lxml')
        for j in find.find_all('a'):
            if j.get('href') != '' and j.get('href') !=  None:
                lst_fin.append(j.get('href'))

    if lst_fin.count(url_refer) > 0:
        return ('Yes')
    else:
        return ("No")

if url_1 != '':

    print(check(url_1, url_refer))

else:
    print('No')


