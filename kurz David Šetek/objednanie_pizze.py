
# Kód z kurzu

# print("Vitajte v aplikácii na objednanie pizze.")
# size = input("Zadajte veľkosť pizze: S, M, L\n")
# chilli_peppers = input("Chcete aj feferóny? A/N\n")
# extra_cheese = input("Chete pridať syr? A/N\n")

# bill = 0

# if size == "S":
#     bill += 4

# elif size == "M":
#     bill += 6

# elif size == "L":
#     bill += 8

# if chilli_peppers == "A":
#     if size != "S":
#         bill += 2
#     else:
#         bill += 1

# if extra_cheese == "A":
#     bill += 1.50

# print(f"Za pizzu zaplatíte {bill}€.")


# Môj kód

print("Vitajte v aplikácii na objednanie pizze.")
size = input("Akú veľkosť si vyberiete? S, M, L?\n")
if size == "S":
    bill = 6
    print(f"Vybrali ste si pizzu veľkosti {size} za cenu {round(bill, 2)}€.")
    feferon = input("Chcete feferónky? A/N\n")
    if feferon == "A":
           bill += 1
           print(f"Vybrali ste si pizzu veľkosti {size} s feferónkami za cenu {round(bill, 2)}€.")
    else:
        print(f"Vybrali ste si pizzu veľkosti {size} bez feferóniek za cenu {round(bill, 2)}€.")

elif size == "M":
    bill = 8
    print(f"Vybrali ste si pizzu veľkosti {size} za cenu {round(bill, 2)}€.")
    feferon = input("Chcete feferónky? A/N\n")
    if feferon == "A":
        bill += 2
        print(f"Vybrali ste si pizzu veľkosti {size} s feferónkami za cenu {round(bill, 2)}€.")
    else:
        print(f"Vybrali ste si pizzu veľkosti {size} bez feferóniek za cenu {round(bill, 2)}€.")

elif size == "L":
    bill = 10
    print(f"Vybrali ste si pizzu veľkosti {size} za cenu {round(bill, 2)}€.")
    feferon = input("Chcete feferónky? A/N\n")
    if feferon == "A":
        bill += 2
        print(f"Vybrali ste si pizzu veľkosti {size} s feferónkami za cenu {round(bill, 2)}€.")
    else:
        print(f"Vybrali ste si pizzu veľkosti {size} bez feferóniek za cenu {round(bill, 2)}€.")

cheese = input("Chcete syr? A/N\n")
if cheese == "A":
    bill += 1.50
    print(f"Cena pizze je {round(bill, 2)}€.")
else:
    print(f"Vybrali ste si pizzu veľkosti {size} bez syru za cenu {round(bill, 2)}€.")