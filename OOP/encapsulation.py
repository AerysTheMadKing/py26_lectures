# Инкапсуляция:

# 1. Связь данных с методами которые должны управлять этими аттрибутамию

# 2. Механизм языка, который позволяет ограничить доступ к определенным компонентам класса.


# Инкапсуляция как связь


# class Phone:
#     number = '+996700700700'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')


# my_phone = Phone()

# my_phone.print_number()




# Инкапсуляция как упарвление доступом

# 3 уровня доступа в питоне

# 1. Публичный (public) - number, print_number

# 2. Защищенный (_protected, parent/child) - _number

# 3. Приватный(__private, толко в текущем классе) - __number 


# class Car():

#     _country = 'Germany'


#     def __init__(self) -> None:
#         self.marka = 'Mercedes-Benz' # public
#         self._model = 'w140' # protected
#         self.__motor = 'ABC' # private

    
# obj = Car()
# print(obj.marka)
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)



# class Phone:

#     username = 'john Snow'
#     _caller = 'Jamie Lanister'
#     __count_of_calls = 15


#     def call(self):
#         print(f'{self._caller} calling')

#     def __increment_of_calls(self):
#         self.__count_of_calls+=1

#     def turn_on(self):
#         print(f'{self.username} взял трубку!')
#         self.__increment_of_calls()


#     def get_count(self):
#         print(self.__count_of_calls)


# obj = Phone()
# obj.call()
# obj.get_count()
# obj.turn_on()
# obj.get_count()



#getter & setter

# Они используются для получения и установки значений в Приватный аттрибуты, чтобы избежать прямого доступа к приватному аттрибуты и еще с помошью сеттеров и геттеров можно добавлять логику проверки при получении данных


# class Person:

#     def __init__(self, name) -> None:
#         self.name = name
#         self.age = 0

#     def display_info(self):
#         print(f'My name is {self.name}, I\'m {self.age} years old!')



# john = Person('John')
# john.display_info()


# class Person:

#     def __init__(self, name) -> None:
#         self.__name = name
#         self.__age = 0

#     def display_info(self):
#         print(f'My name is {self.__name}, I\'m {self.__age} years old!')

    
#     def get_name(self):
#         return self.__name


#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Invalid value!')

#         else:
#             self.__name = name

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age <150:
#             print('Invalid value for age!')

#         else:
#             self.__age = age


# john = Person('John')

# john.display_info()

# john.set_name(None)

# john.set_age(-18)

# john.display_info()

# john.set_name('Jamie')

# john.set_age(24)
# john.display_info()




# class Russia:
#     __name = 'Russian Federation'
#     __population = 0


#     def get_population(self):
#         return self.__population

#     def set_population(self, num):
#         if not isinstance(num, int) or num < 0:
#             print('Invalid value to population!')

#         else:
#             self.__population = num

#     def get_name(self):
#         return self.__name


#     def display_info(self):
#         print(f'Population of {self.get_name()}: {self.get_population()}')



# obj = Russia()

# obj.set_population(143_000_000)
# obj.display_info


# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.__age = 0

#     def _age_increment(self):
#         self.__age += 1


#     def birthday(self):
#         print(f'Today {self.name}s birthday!')
#         self._age_increment()

#     def display_info(self):
#         print(self.name, self.__age)

# obj = Person('John')
# obj.display_info()
# obj.birthday()
# obj.display_info()


"""
1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
"""

# class Person:
    
#     def __init__(self) -> None:
#         pass
        

        

#     def username(self):
#         print('Публичный метод!')

#     def _user_age(self):
#         print('Защищенный метод!')

#     def __user_work(self):
#         print('Приватный метод!')


# armstrong = Person()
# armstrong.username()
# armstrong._user_age()
# armstrong._Person__user_work()


# class CRUD:
#     __product = []
#     __id = 0

#     def _get_id(self):
#         self.__id += 1
#         return self.__id
    
#     def _get_product(self, id):
#         for x in self.__product:
#             if x['id'] == id: return x
#         return False


#     def create(self):
#         print("CREATE of product!")
#         title = input('Enter title: ')
#         price = input('Enter price: ')
#         self.__product.append(
#             {'id':self._get_id(),
#              'title': title,
#               'price': price
#               })

#     def list_of_product(self):
#         print('Все наши продукты: ')
#         for x in self.__product:
#             print(x['title'])

    
#     def detail_product(self):

#         id = int(input('Enter ID product: '))
#         product = self._get_product(id)
#         print(product if product else 'нет такого продукта')
    

#     def update_product(self, id):
#         print('update')
#         id = int(input('введите id продукта: '))
#         product = self._get_product(id)
#         if not product:
#             print('нет такого продукта')
#             return
#         choice = input('что изменить(title/price): ')
#         index = self.__product.index(product)
#         self.__product[index][choice] = input('введите новое значение: ')

    
#     def delete_product(self):
#         print("DELETE")

#         id = int(input("Enter ID product: "))
#         product = self._get_product(id)

#         if not product:
#             print('Нет такого продукта!')
#             return 

#         self.__product.remove(product)

#         print('Удалено!')

        

        

    
# product = CRUD()
# product.create()
# product.create()
# product.list_of_product()

# product.detail_product()
# product.detail_product()
# product.update_product(id)
# product.detail_product()
# product.delete_product()
# product.list_of_product()

 
