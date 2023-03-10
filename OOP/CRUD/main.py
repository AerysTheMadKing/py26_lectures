from views import CreateMixix, ReadMixin, UpdateMixin, DeleteMixin


class Product(CreateMixix, ReadMixin, UpdateMixin, DeleteMixin):

    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent = 4 )

        return 'Saved!'

smartphones = Product()
print(smartphones.post(title = 'Redmi Note 10', description = 'The best phone for own price', qty = 10, price = 250))

print(smartphones.post(title = 'Iphone 13 Pro Max', description = 'created for crudles', qty = 5, price = 1200))

print(smartphones.post(title = 'Samsung A22 Ultra', description = 'The best phone for android lovers', qty = 6, price = 1000))

print(smartphones.post(title = 'HUAWEI', description = 'The best phone for lovers smartphone games', qty = 5, price = 500))

print(smartphones.post(title = 'Tesla X20', description = 'Future smartphone', qty = 4, price = 1500))

print()
print()

print(smartphones.list())
print()

print(smartphones.detail(5))
print(smartphones.detail(15))
print()

print(smartphones.patch(5, title = 'Tesla X25'))
print(smartphones.patch(15, title = 'Tesla X25'))
print()
print(smartphones.delete(5))
print()
print(smartphones.list())
print(smartphones.save())