"""
1) Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.

У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.

Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.

класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.
"""
class CreateMixin:

    def create(self, todo, key):
        if key in self.todos:
            print("Задача под таким ключём уже существует")
        return key[todo] == self.todos

class DeleteMixin:

    def delete(self,todo, key):
        self.todos.pop(key)
        print(f'удалили {todo} задачу')

class UpdateMixin:
    
    def update(self, key, new_value):
        self.todos.update({key: new_value})

class ReadMixin:

    def read(self):
        self.todos.sorted()


import datetime 
class Todo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}

    def set_deadline(self):
        a = datetime.datetime.now()
        print(a.day)

todo = Todo()
todo.delete(5)

