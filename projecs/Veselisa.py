import random
 
cars_name = ["audi","bmw", "ford", "hyundai", "honda", "kia", "lada", "mazda", "mercedes-benz", "mitsubishi", "nissan", "renault", "skoda", "toyota", "wolkswagen", "lexus", "subaru", "suzuki", "cadillac", "tesla"]
word=cars_name[random.randrange(0, len(cars_name))]
len_word=len(word)
attempt = 7
test=False
used_letters=""
ls=[]

for i in range(len(word)):
    ls+="*"
 
while len_word != 0 and attempt!= 0:
    test = False
    while True:
        letter = input("\nвведите букву ")
        if letter in used_letters or len(letter)>1:
            print("\nНе больше одного символа, попробуйте снова!")
        else:
            used_letters+=letter
            break
    count=0
    for i in word:
        if letter in i:
            len_word -= 1
            test=True
            ls[count]=letter
        count+=1
 
 
 
    if not test :
        attempt -= 1
        print("Неверно")
    else:
        print("Верно")
        print(ls)
 
    print("Ваше здоровье = ", attempt)
 
if(len_word == 0):
    print("\nПОБЕДИТЕЛЬ!!! Слово было", word.lower())
else:
    print("\nВЫ ПРОИГРАЛИ! ПОПРОБУЙТЕ СНОВА!")

        



















