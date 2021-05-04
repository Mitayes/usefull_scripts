from xlsx2csv import Xlsx2csv
import datetime
import os
import re


# Функция, принимает аргументом 1 путь к папке, внутри которой размещены файлы xlsx, папок внутри быть не должно!
def __convert_xlsx2csv__(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            fullname = os.path.join(root, name)
            if os.path.isfile(fullname):
                outname = os.path.join(root, 'converted', re.sub(r'.xlsx', '.csv', name))
                # Тут указывается кодировка и разделитель, sheetid=0 - значит, что конвертим все листы из книги,
                # иначе пишем номер нужного листа
                Xlsx2csv(fullname, outputencoding="utf-8", delimiter='#').convert(outname, sheetid=0)


if __name__ == '__main__'
	# Отмечаем время старта скрипта
	start_time = datetime.datetime.now()

	# Вызываем функцию для конвертирования. Путь к папке с файлами указывается без \ на конце
	__convert_xlsx2csv__(r'D:\test')
	
	# Вычисляем и выводим расчётное время выполнения скрипта
	end_time = datetime.datetime.now()
	print("total time", str(end_time - start_time))
