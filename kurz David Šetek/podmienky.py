# print("Vitajte na horskej dráhe")
# height = float(input("Aká je vaša výška (v cm)?\n"))

# if height >= 87:
#     print("Môžete pokračovať na dráhu")
# else:
#     print("Nemáte povolený vstup na dráhu")

# age = int(input("Zadaj svoj vek\n"))
    
# if age < 18:
#     print("Si neplnoletý")
# else:
#     print("Nech sa páči")

print("Vstupné do kina")
student = input("Si študent? Odpovedez áno/nie\n")

if student == "áno" or student == "hej" or student == "som":
    print("Cena lístku je 5€")
elif student == "nie" or student == "ni" or student == "ee":
    print("Cena lístku je 7€")
else:
    print("Zadaj odpoveď")