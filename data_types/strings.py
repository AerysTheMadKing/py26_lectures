
'=====================Тип данных-Строки================='

'Строки(str) - это набор последовательных символов, которые мы используем для хранения и представления текстовой информации.'

'index - это нумерация каждого элемента(символа) в строке, индексация всегда начинается с 0'

name = 'John Snow'
'       012345678   '
        # J = 0
        # o = 1 
        # h = 2
        # n = 3
        # ...

'========================= Срезы ==========================='

'Срезы по индексам - это когда мы получаем определенную часть строки при помощи индексов'

'Срезы[start : end(не включительно) : step]'

'start - начало среза, начальный индекс, по умолчанию стоит 0-ой индекс'
'end - конец среза, конечный индекс, который не включителен, по умолчанию берет до конца'
'step - шаг среза, который указывает через сколько элементов проходиться, по умолчанию стоит 1'

# name = 'John Snow Man'

# snow_1 = name[5:9] #Snow
# snow_2 = name[5:]  #Snow Man, end не указали поэтому он возьмет до конца

# print(snow_1) #Snow
# print(snow_2) #Snow Man

# name = 'John Snow Man'

# john_1 = name[0:4]
# john_2 = name[:4]

# print(john_1) #John
# print(john_2) #John

# name = 'john snow man'

# step_2 = name[0:13:2]
# step_3 = name[0:13:3]

# print(step_2) #jOhN SnOwmAn -> jh nwmn
# print(step_3) #jOHnSnOW MAn -> jnn n 

# name = 'JhonklasjdklaSJDLJAKSJDJASKLDJKLASJDKLASJDKASDJASKNCFKJASultanSNDKJASNDKJAFJHWIQOE12391829038192LMS,M,D,MDSm,smdm,ms'

# print(name[-10])

# name = 'John Snow Man'
# reversed_name = name[::-1] # naM wonS nhoJ
# print(reversed_name) # naM wonS nhoJ

#Перевернутая строка(reverse)
# name = 'John Snow Man' 
# reversed_name_naM = name[12:9:-1] #naM
# reversed_name_wnoS = name[8:4:-1] #wonS
# print(reversed_name_naM)
# print(reversed_name_wnoS) 

#Склеивание строк(конкатенация)
# first_name = 'Sultan'
# second_name = 'Talaibekov '
# full_name = first_name + ' ' + second_name
# print(full_name) #Sultan Talaibekov

# print(full_name*2) #Sultan Talaibekov Sultan Talaibekov
# print(full_name*2.5) # error


'===============Форматирование строк=========='
'''
Способы(3 вида):
1) с помощью %s
2) с помощью (.format())
3) интерполяция строк(f'строка')
'''

# 1) %s

# name_1 = input('Введите свое имя: ')
# name_2 = input('Введите свое имя: ')
# print('Привет, меня зовут', name, 'Talaibekov')

# print("Привет, меня зовут"+ ' ' + name + ' ' + 'Talaibekov')
# age = 25
# print('Привет, %s, мне %s лет' %(name_2, age))



#2) .format()

# name = input('Введите свое имя: ')
# age = 25
# result = 'Привет, мое имя {}, мне {} лет' .format(name, age)
# print(result)


#3) f'строки'

# name = input('Введите свое имя: ')

# result = f'Привет, {name}, как твои дела?'
# print(result)


'======================Экранирование строк================='

"""
\n - перенос строки
\t - горизонтальная табуляция
\v - вертикальная табуляция
"""

# print('hello world\nmy name is Anton\nI\'m Sabina\'s mom')
# print('Hello world\n\tmy name is Gustaph')
# print('Hello world\vSup')
# print('Hello world\n\tSup')



'16.12.22'

# num_list = [102, 90, 36]

# smallest_num = min(num_list)

# print(smallest_num)








        





