
import random
name = input("Назовите свое имя: ")
game = input("Хотите играть в игру угадай число: ")

number_of_attempts = 0
random_=random.randint(1,10)
print(random_)
while True:
    number_of_attempts += 1
    print(f"Ваша {number_of_attempts} попытка!")
    
    
    if game.lower() == "да":
        pass
        
    else:
        print("Спасибо")
        break

    number = int(input("Угадай число: "))

    if number == random_:
        print(f"Число было {random_}\nВам потребовалось,{number_of_attempts} попыток чтобы отгадать число.")
        game1 = input("Хотите продолжить: ")
        if game1.lower() == "да":
            number_of_attempts = 0
            random_=random.randint(1,10)
            pass
        else:
            print("Спасибо")
            break
        
    elif number_of_attempts > 4:
        print(f"число было {random_}, вы не угадали!")
        break
    



    
        











    