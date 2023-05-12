x1 = int(input("Введите координаты первой клетки:\nx:"))
y1 = int(input("y:"))
x2 = int(input("Введите координаты второй клетки:\nx:"))
y2 = int(input("y:"))

if any(x > 8 or x < 1 for x in [x1, x2, y1, y2]):
    print("Неверные значения")
    exit()
if x1 == x2 and y1 == y2:
    print("Вы не походили")
    exit()
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")