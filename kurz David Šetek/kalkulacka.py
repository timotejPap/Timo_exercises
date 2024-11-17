
# Kalkulačka na výpočet platieb

# 1. option
# print("Vitajte v kalkulačke na výpočet platieb")
# max_price = float(input("Zadaj celkovú sumu\n"))
# percentage = float(input("Koľko chcete dať spropitné v %?\n"))
# people = int(input("Medzi koľkými ľuďmi sa má rozdeliť čiastka?\n"))

# tip = (percentage/100)*max_price
# total_price = max_price + tip
# price_per_person = total_price / people
# print(f"Každý čovek má zaplatiť {price_per_person} Eur")

# 2. option

print("Vitajte v kalkulačke na výpočet platieb")
max_price = float(input("Zadaj celkovú sumu\n"))
percentage = float(input("Koľko chcete dať spropitné v %?\n"))
people = int(input("Medzi koľkými ľuďmi sa má rozdeliť čiastka?\n"))

one_payment = (max_price + (max_price / 100 * percentage)) / people
print(f"Každý človek zaplatí {"{:.2f}".format(one_payment)} Eur")