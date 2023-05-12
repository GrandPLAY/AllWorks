import random

list1 = []
list2 = []
gustoy_list = []

for i in range(random.randint(1, 10)):
    list1.append(random.randint(1, 10))
for i in range(random.randint(1, 10)):
    list2.append(random.randint(1, 10))

for i in range(min(len(list1), len(list2))):
    gustoy_list.append(list1[i])
    gustoy_list.append(list2[i])

for j in range(i+1, len(list1)):
    gustoy_list.append(list1[j])
for j in range(i+1, len(list2)):
    gustoy_list.append(list2[j])

print("Первый список:", list1)
print("Второй список:", list2)
print("Итоговый список:", gustoy_list)
