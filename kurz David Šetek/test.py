# print("Ahoj")

# print("Dobrý deň")
# print("Timotej\nprezývka'Timčo'")
# print("Pap")

# # thisis comment

# print("Učím sa Python")
# print("Funkcia print začína slovom print")
# print('Funkciu print zavoláme print ("nejaký text")')


# print("Timotej\nadmin123")
# print("Harry" + " " + "Ron" + " " + "Hermiona")

# print("Naučili sme sa o stringu")
# print('Spojenie stringu robíme pomocou znamienka "+"')
# print("Tiež sme používali print ('nejaký text')")
# print("Prvý riadok\nDruhý riadok")

# print("Ahoj, ja som " + input("Zadaj meno\n"))

# name = input("Zadaj meno\n")
# print("Ahoj, ja som " + name)

# age = 40
# age = 40 + 10
# print(age)

# city = input("Zadaj bydlisko\n")
# print("Bývam v meste " + city)

# greeting = ("Ahoj Peťo")
# print(len(pozdrav))

# length = len(input("Zadaj meno\n"))
# print("Tvoje meno má", length, "znakov")


# String
# print("Ahoj" [0])
# print('Python' [3], 'malo by byť písmeno "h"')

# # Integer
# print(15)
# print(35+15)
# print(123456)
# print(123_456)

# # Float
# print(3.14)
# print(15+12.5)

# Boolean
# True
# False

# age = 33
# number = 40.8
# print(type(age))

# age = str(40)
# print(type(age))

# print("Ahoj, ja som Timo a mám " + str(age) + " rokov")


# set_number = (input("Napíšte dvojmiestne číslo:\n"))
# first_num = int(set_number [0])
# second_num = int(set_number [1])
# print(first_num + second_num)
 
# print(8 / 3)
# print (int(8 / 3))
# print(8 // 3)

# print(round(8 / 3, 2))

# weight = input("Zadaj váhu v kg:\n")
# height = input("Zadaj výšku v metroch:\n")

# BMI = int(weight) / float(height)**2
# print(BMI)
# BMI = round(BMI, 2)
# print("Vaše BMI je: ", BMI)

# x = (1)
# # x = x + 1
# x += 1
# print(x)

# F-string
# x = (5)
# print(f"Hodnota x je: {x}")
# print("X má hodnotu", x)

# name = ("Timo")
# age = (33)
# print(f"Volám sa {name} a mám {age} rokov")


# Výpočet zvyšného veku, mesiacov, týždňov a dní

# age = int(input("Zadaj svoj vek\n"))
# max_age = 90
# years = max_age - age
# months = 12 * years
# weeks = 52 * years
# days = 365 * years
# print(f"Ostáva vám {years} rokov, {months} mesiacov, {weeks} týždňov, alebo {days} dní")

# print(f"Ostáva vám {90-age} rokov, {(90*12)-(age*12)} mesiacov, {(90*52) - (age*52)} týždňov, alebo {(90*365) - (age*365)} dní")

# modulo
# print(6 % 4)
# print(10 % 3)
# print(12 % 10)

# number = int(input("Zadaj celé číslo:\n"))
# if number % 2 == 0:
#     print("Číslo je párne.")
# else:
#     print("Číslo je nepárne.")


            # Horská dráha + nayvýšenie vstupného

print("Vitajte na horskej dráhe")
height = float(input("Aká je vaša výška (v cm)?\n"))
bill = 0

if height >= 87:
    print("Môžete pokračovať na dráhu")
    age = int(input("Zadaj svoj vek\n"))
    if age <= 12:
        bill = 4
        print("Vstupné je 4€.")
    elif age <= 18:
        bill = 6
        print("Vstupné je 6€.")
    elif age >= 40 and age <= 50:
        # bill = 0
        print("Vstupné je zdarma.")
    else:
        bill = 8
        print("Vstupné je 8€.")
        
    photo = input("Chcete sa počas jazdy nechať vyfotiť? Áno/Nie\n")
    if photo == "Áno":
        bill += 2
    print(f"Cena vstupného bude {bill}€.")
else:
    print("Nemáte povolený vstup na dráhu.")