
number = 25
while number > 10:
    number -= 5
    print(number)


slovo = "Kocka"
for i in range(0, 10, 2):
    print(i, slovo)

pocitadlo = 0
while True:
    print(pocitadlo)
    if pocitadlo >= 4:
        break
    pocitadlo += 1
print("Hotovo")

cisla = (1, 2, 3, 4, 5)
for i in cisla:
    print(i, cisla[2])

string = "Informatika s Misom"
for character in string:
    print(character)
    if character == "a":
        print("x")

counter = 1
while counter < 10:
    counter += 1
    if counter % 2 == 1:
        continue
    print(counter)

for riadok in range(1, 5):
    for stlpec in range(1, riadok):
        print(stlpec)