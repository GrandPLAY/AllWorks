def func1(length):
    m = round(length)
    cm = round((length - m) * 100)
    mm = round((length - m - cm/100) * 1000)
    print("Введенная длина:", m, "м,", cm, "см,", mm, "мм")


length = float(input("Введите длину в метрах: "))
func1(length)
