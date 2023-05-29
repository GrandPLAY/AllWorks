word = input("Введите слово: ")
if word == word[::-1]:
    print(word, "- палиндром")
else:
    print(word, "- не палиндром")
