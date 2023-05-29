matrica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrica2 = [[matrica[0][2], matrica[1][2], matrica[2][2]], [matrica[0][1], matrica[1][1], matrica[2][1]], [matrica[0][0], matrica[1][0], matrica[2][0]]]

for row in matrica:
    for elem in row:
        print(elem, end=' ')
    print()
print()
for row in matrica2:
    for elem in row:
        print(elem, end=' ')
    print()
