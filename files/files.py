# Работа с файлами

# Каретка - Указатель - Курсор

# open(<путь до файла>)

# file = open('/home/bayel/Desktop/makers/files/files.py') # Абсолютный путь

# file = open('files.py') # Относительный путь
# ~ working -> Desktop/makers/files/files.py
# makers -> files/files.py

# file = open('files/files.py')
# data = file.read()
# print(type(data))
# file.close()

# Режимы работы с файлами
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)
# b, x


# file = open('files/test.txt', 'r')
# print(file.read())
# file.close

# file = open('files/test.txt', 'r')
# data = file.readlines()
# print(data)
# print(len(data[0]))
# file.close()

# file = open('files/test.txt', 'r')
# print(file.readline())
# print('!!!!')
# print(file.read())
# file.close()


# Контекстный менеджер
# with open('files/test.txt', 'r') as file: #file = open('files/test.txt')
#     data = file.read()
#     print(data)
#     print(file, 'inside')

# print(file, 'outside')


# with open('files/test.txt', 'r') as f:
#     print(f.tell())
#     data = f.read(20)
#     print(f.tell())
#     print(data)
#     print(f.read())
#     print(f.tell())

# file.tell() -> возвращает индекс, где находится указатель(курсор)
# file.seek(index) -> перемещает курсор на индекс, который вы передали

# with open('files/test.txt', 'r') as file:
#     print(file.readline())
#     file.seek(0)
#     print(file.readline())
#     file.seek(0)
#     a = file.read()
#     print(file.readline())
#     # print(file.readlines())

# print(a)

# with open('files/test.txt', 'w') as file:
#     # file.write('Первая строчка!')
#     # file.write('\nHe is bastard of Ned Stark!\n')
#     # file.write('This is lesson about files!')
#     # file.seek(0)
#     data = ['Первая строчка!\n', 'He is bastard of Ned Stark!\n', 'This is lesson about files!']
#     file.writelines(data)

# with open('files/test.txt', 'a+') as file:
#     file.write('\nJohn Snow is North King!')
#     file.write('\nYou know nothing John Snow!')
#     file.seek(0)
#     print(file.read())

'-------------------------------------------------------------------------'

# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re

# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     # print(string)
#     # print(type(string))
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)
#         # for x in list_of_imei:
#         #     file.write(f'{x}\n')

# image = 'imei.jpg'
# get_imei_code(image)

# """"""
# "r" - "read"
# "r+" - "read + write"
# "w" - "write"
# "w+" - "read + write"
# "a" - "append"
# "a+" - "append + read"

# >>>>
# "x" - "write" # он открыт для записи в том случае если файла нет. если такого файла не существует он открывает и запишет туда.
# "b" - "binary" #открывает бинарный файл (двоичным режиме)
# "t" - "text" # открывает текстовый файл
# "rt" - # открываем файл в текстовом режиме.
# "rb" - # открываем файл в бинарном режиме.
# >>>>

# seek(0) - (курсор) начинает с самого начало.