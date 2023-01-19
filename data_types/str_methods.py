'================================== Методы строк============================='

# print(dir(str)) # список методов

'REPLACE' 

# str.replace (старое значение, новое значение, кол-во) - это метод строк, который меняет старое
# значение на новое если указать количество еще меняет столько сколько раз мы указали кол-во

# text = 'ha ha ha ha'
# result = text.replace('a', 'o', 2)
# print(result) # ho ho ha ha

# text = 'name Isaev'
# result = text.replace('name', 'Nuuman')
# print(result) # Nuuman Isaev




'STRIP'
#str.strip() - метод строк, который убирает пробелы в начале и в конце строки.


# text = '   hello world   '
# result = text.strip()
# print(text) #  '     hello world    '
# print(result) # 'hello world'

# print(len(text))
# print(len(result))




#str.rstrip - убирает пробелы с права ( в конце)

# text = '    hello world     '
# result = text.rstrip()# убирает справа все пробелы
# print(result) # '    hello world'
# print(len(text.rstrip())) # 15 



#str.lstrip - убирает пробелы с лева( в начале)

# text = '    hello world     '
# result = text.lstrip()# убирает слева все пробелы
# print(result) # hello world     '
# print(len(text.rstrip())) # 16



'ISDIGIT, ISNUMERIC,ISDECIMAL'

#str.isdigit()
#str.isnumeric() - это методы строк которые проверяют являются ли наша строка полностью из чисел
#str.isdecimal()

# text = '25'
# print(text.isdigit())
# print(text.isnumeric())
# print(text.isdecimal())

# age = input('Введите свой возраст: ')
# print(age.isdigit())



'ISALPHA'
#str.isalpha() - это метод, строк который проверяет состоит ли наша строка только из латинцы или киррилицы.

# text = 'asd-==-=vfvf'
# print(text.isalpha()) # False  он не берут символов.

# text = 'american boy'
# print(text.isalpha()) # False так ка пробел не киррилица или латинца.

# text = 'americanboy'
# print(text.isalpha()) # True, так как вся строка состоит из лaтинцы.




'ISALNUM'
# #str.isalnum() - это метод, который проверяет на то что состоит ли наша строка из чисел и символов латинского или киррильского алфавита.

# text = 'album21'
# print(text.isalnum()) # True,  так как строка состоит из латинцы и чисел.

# text = 'album 21 = + '
# print(text.isalnum()) # False , так как есть символы (пробелы, плюс, равно и т,д)

# text = '123345'
# print(text.isalnum()) # True  




'ISLOWER, ISUPPER'

#str.islower()-  метод строк, который проверяет на нижний регистр(с маленькой буквой)

#str.isupper() -  метод строк ,который проверяет на верхний регистр(с  большой буквой)

# text = 'makers'
# print(text.islower()) # True
# print(text.isupper()) # False

# text2 = 'MaKers'
# print(text2.islower()) # False
# print(text2.isupper()) # False

# text3 = 'makers1234'
# print(text3.islower()) # False
# print(text3.isupper()) # False

# text4 = 'MAKERS1234'
# print(text4.islower()) # False
# print(text4.isupper()) # True




'ISTITLE'

#str.istitle() - это метод, строк который проверяет начинается ли каждое слово в строке  с верхнего регистра(с большой буквы)



# name = 'nuuman isaev'
# name2 = 'Nuuman Isaev'
# print(name.istitle()) # False
# print(nam2.istitle()) # True

# name = 'Nuuman isaev'
# print(name.istitle()) # False  каждая буква дольжен начинатся с большой буквой


'INDEX'

#str.index(values, start,end) - это метод строк который возврашает индекс заданого значения(values)


# text = 'makers bootcamp'
# print(text.index('a', 7)) # 12, ищет в слове bootcamp




'COUNT'
#str.count() (values,start) - метод строк который счетает сколько у нас значений (values) есть в строке

# text = 'codingiseasyhfkfhkfhki'
# print(text.count('i')) # 3 начинает искать от начала до конца

# print(text.count('i',5)) # 2  начинает искать с 5 индекса до конца

# print(text.count('i', 5,9)) # 1 начинает искать с 5 индекса до 9 (не исключительно)





'FIND'
#str.find()(values, start,end) - это метод строк, такой же как и метод строк str.index(смотрите выше), но он не выведет ошибку, если значения (values) нету в строке, он просто вернет индекс -1.

# text = 'makers bootcamp'
# print(text.find('z')) # распечатает -1

# text = 'makers bootcamp'
# print(text.index('z')) # распечатает ValueError(not found)



'SWAPCASE'

#str.swapcase() - это метод строк который меняет на противоположный  регистр (a->A), (A->a) (makers)->(MAKERS) (makErs)->(MaKeRS)

# text = 'codingiseasy'
# print(text.swapcase()) # SWAPCASE

# text1= 'CODINGISEASY'
# print(text2.swapcase()) # codingiseasy

# text3 = 'CodinGisEASy'
# print(text3.swapcase()) # cODINgISeasY

# text4 = input('Enter your text: ') #Nuuman
# print(text4.swapcase()) # nUUMAN 



'CAPITALIZE'
#str.capitalize() - это метод строк, который меняет первую букву строки на верхний регистр, остальные на нижний.

# text = 'hi, my name is Anton' # Hi, my name is anton
# print(text.capitalize())


'TITLE'

#str.title() - это метод строк, который переводит начало каждого слова в строке в верхний регистр.

# text = 'hi, my name is ghustaph'
# print(text.title()) # Hi, My Name Is Ghustaph




'SPLIT'
#str.split(разделитель) - это метод строк ,который строку переводит в лист при помощи разделителя.

# text = 'Hi, my name is Nuuman'
# print(text.split()) # ['Hi', 'my', 'name', 'is', 'Nuuman']


'JOIN'
#'соединитель'.join(str) - это метод строк ,который соединяет элементы листа.

# list_  = ['12','23','54','25']
# print(''.join(list_)) # 12235425

# list_  = ['12','23','54','25']
# print('*'.join(list_))ъ # 12*23*54*25


# print(dir(str))






























































