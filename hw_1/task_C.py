mas = []

for i in range(4):
    mas.append(input())

print()

for i in range(len(mas)):
    if len(mas[i]) >= 10:
        if mas[i][0] == "8":
            mas[i] = mas[i].replace("8", "+7", 1)

    new_number = ""
    for j in range(len(mas[i])):
        if mas[i][j] != "(" and mas[i][j] != ")" and mas[i][j] != "-":
            new_number += mas[i][j]
    mas[i] = new_number

for i in range(len(mas)):
    if len(mas[i]) < 10:
        mas[i] = "+7495" + mas[i]

print(mas)

if mas[0] == mas[1]:
    print("YES")
else:
    print("NO")

if mas[0] == mas[2]:
    print("YES")
else:
    print("NO")

if mas[0] == mas[3]:
    print("YES")
else:
    print("NO")
