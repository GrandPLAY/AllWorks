import random


list = []
find = False

for i in range(random.randint(1, 100)):
    list.append(random.randint(1, 100))

print("Массив: " + str(list))

try:
    check = int(input("Введите необходимую сумму индексов (до 200): "))
except:
    print("Эээ, ты что-то не то ввел. Программа закрывается")
    exit()

if check > 200:
    print("Ну я просил же не больше 200. Программа закрывается")
    exit()
elif check < 1:
    print("Я где тебе такую сумму достану? Программа закрывается")
    exit()
else:
    for i in range(len(list)):
        for j in range(len(list)):
            sum = list[i] + list[j]
            if sum == check:
                print("Я нашел! " + str(check) + " будет если сложить индексы " + str(i) + " и " + str(j))
                find = True
if not find:
    print("Я ничего не нашел(")
