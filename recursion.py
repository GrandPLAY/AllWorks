import random


def cut(list, check):
    if len(list) != 1:
        if check >= list[len(list) // 2]:
            list = list[len(list) // 2:]
            print(list)
        else:
            list = list[:len(list) // 2]
            print(list)
        cut(list, check)
    else:
        if list[0] != check:
            print("Числа нет в списке")



list = []

for i in range(random.randint(1, 10000000)):
    list.append(random.randint(1, 10000000))

list.sort()

print("Массив: " + str(list))

try:
    check = int(input("Введите искомое число: "))
except:
    print("Эээ, ты что-то не то ввел. Программа закрывается")
    exit()

cut(list, check)
