def length(name, age):
    age_word = age_to_words(age)
    name_len = len(name)
    age_len = len(age_word)
    total_len = name_len + age_len
    print(name, age, "(", age_word, "), количество символов:", total_len)


def age_to_words(age):
    age_dict = {
        0: "ноль",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать",
        20: "двадцать",
        30: "тридцать",
        40: "сорок",
        50: "пятьдесят",
        60: "шестьдесят",
        70: "семьдесят",
        80: "восемьдесят",
        90: "девяносто"
    }

    if age in age_dict:
        return age_dict[age]
    elif age < 100:
        tens = (age // 10) * 10
        ones = age % 10
        return age_dict[tens], age_dict[ones]
    else:
        return "неизвестно"

name = input("Введите имя: ")
age = int(input("Введите возраст числом: "))
length(name, age)
