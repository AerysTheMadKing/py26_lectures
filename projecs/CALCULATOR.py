python = int(input("Введите первое число: "))
backend = int(input("Введите второе число: "))
operation = input("Выберите операци:")

if operation== "+":
    print(f'Ответ:',python+backend)

elif operation == "-":
    print(f'Ответ:',python-backend)

elif operation == "*":
    print(f'Ответ:',python*backend)

elif operation == "/":
    print(f'Ответ:',python/backend)

elif operation == "%":
    print(f'Ответ:',python%backend)

elif operation == "**":
    print(f'Ответ:',python**backend)

elif operation == "//":
    print(f'Ответ:',python//backend)


else:
    print("Данной операция нет в системе!")



