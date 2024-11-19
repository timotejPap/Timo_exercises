
            # Podmienka na horskú dráhu (výška)

# print("Vitajte na horskej dráhe")
# height = float(input("Aká je vaša výška (v cm)?\n"))

# if height >= 87:
#     print("Môžete pokračovať na dráhu")
# else:
#     print("Nemáte povolený vstup na dráhu")


            # Plnoletosť

# age = int(input("Zadaj svoj vek\n"))
# if age < 18:
#     print("Si neplnoletý")
# else:
#     print("Nech sa páči")


            # Vstupné do kina
# print("Vstupné do kina")
# student = input("Si študent? Odpovedez áno/nie\n")

# if student == "áno" or student == "hej" or student == "som":
#     print("Cena lístku je 5€")
# elif student == "nie" or student == "ni" or student == "ee":
#     print("Cena lístku je 7€")
# else:
#     print("Zadaj odpoveď")


            # Typ mobilného telefónu

# type = input("Aký typ mobilu chcete? Možnosti: normal, smart, extrasmart\n")

# if type == "normal":
#     print (f"Vybrali ste si model {type} za cenu  200€")
# else:
#     print (f"Vybrali ste si model {type} za cenu  350€")


# type = input("Aký typ mobilu chcete? Možnosti: normal, smart, extrasmart\n")

# if type != "normal":
#     print (f"Vybrali ste si model {type} za cenu  350€")
# else:
#     print (f"Vybrali ste si model {type} za cenu  200€")


            # Horská dráha s elif
# print("Vitajte na horskej dráhe")
# height = float(input("Aká je vaša výška (v cm)?\n"))

# if height >= 87:
#     print("Môžete pokračovať na dráhu")
#     age = int(input("Zadaj svoj vek\n"))
#     if age <= 12:
#         print("Vstupné je 2€.")
#     elif age <= 18:
#         print("Vstupné je 4€.")
#     else:
#         print("Vstupné je 7€.")
# else:
#     print("Nemáte povolený vstup na dráhu.")
# 
# 
            # Horská dráha + nayvýšenie vstupného
# print("Vitajte na horskej dráhe")
# height = float(input("Aká je vaša výška (v cm)?\n"))
# bill = 0

# if height >= 87:
#     print("Môžete pokračovať na dráhu")
#     age = int(input("Zadaj svoj vek\n"))
#     if age <= 12:
#         bill = 4
#         print("Vstupné je 4€.")
#     elif age <= 18:
#         bill = 6
#         print("Vstupné je 6€.")
#     else:
#         bill = 8
#         print("Vstupné je 8€.")
        
#     photo = input("Chcete počas jazdy vyfotiť? Áno/Nie\n")
#     if photo == "Áno":
#         bill = bill + 2
#         # bill += 2
#     print(f"Cena vstupného bude {bill}€.")
# else:
#     print("Nemáte povolený vstup na dráhu.")


        # Prestupné roky

year = int(input("Zadaj nejaký rok: "))
if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print(f"{year} je prestupný rok.")
        else:
            print(f"{year} je prestupný rok.")
    else:
        print(f"{year} je prestupný rok.")
else:
    print(f"{year} nie je prestupný rok.")