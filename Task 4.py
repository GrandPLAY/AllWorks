text = input("Введите текст:\n")
words = text.split()
maxword = words[0]

for i in range(len(words)):
    if len(words[i]) > len(maxword):
        maxword = words[i]

print(maxword)
