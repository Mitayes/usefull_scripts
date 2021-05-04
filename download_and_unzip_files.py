'''
Структура папок:
\
 list.txt
 zip
    Сюда качаются архивы
 out
    Сюда распаковываются файлы
'''

import os
import shutil
import requests
import datetime


# Задаём имя файла в архиве, чтобы оно переименовывалось после распаковки
pattern = 'test_filename_0000000001.xml'
# Задаём путь к папке, где лежат архивы
path = r'd:\Jupyter\requests\zip'
# Задаём путь к папке, куда будем складывать распакованные файлы
dst = r'd:\Jupyter\requests\out'
# Задаём файл, в котором содержатся кадастрики
list_f = r'd:\Jupyter\requests\list.txt'
# Вычисляем количество файлов, которые будем качать по количеству строк в файле с кадастриками
total_link = sum(1 for line in open(list_f, 'r'))
# Задаём начало ссылки, к которой будем добавлять кадастрик
url_pat = 'http://test_url/59/'
link_number = 0

start_time_down = datetime.datetime.now()
print('Start download files:', start_time_down)

# Начинаем качать файлики по списку
with open(list_f, encoding='utf-8') as link:
    for line in link:
        url = url_pat + line.rstrip()
        link_number += 1
        if link_number % 10 == 0:
            print(link_number, 'of', total_link, 'complete')
        with open(path + '\\' + url.split('/')[-1].replace(':','_') + '.zip', 'wb') as zfile:
            r = requests.get(url)
            zfile.write(r.content)

end_time_down = datetime.datetime.now()
print('End download files:', end_time_down)
print('Total download time:', (end_time_down - start_time_down), '\n')

# Собираем список архивов, которые будем распаковывать
list_zip = os.listdir(path)

start_time_unzip = datetime.datetime.now()
print('Start unzip files:', start_time_down)

# Начинаем распаковку архивов
for i, zipfile in enumerate(list_zip):
    if '.zip' in zipfile:
        fullname = os.path.join(path, zipfile)
        shutil.unpack_archive(fullname, dst)
        try:
            # Пробуем переименовать файл по паттерну
            shutil.move(os.path.join(dst, pattern), os.path.join(dst, pattern[:-4] + '_' + str(i) + '.xml'))
        except:
            pass

end_time_unzip = datetime.datetime.now()
print('End unzip files:', end_time_down)
print('Total unzip time:', (end_time_unzip - start_time_unzip), '\n')
print('Total script time:', (end_time_unzip - start_time_down))
