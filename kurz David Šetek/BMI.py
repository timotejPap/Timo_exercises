
            # BMI calculator

# weight = input("Zadaj váhu v kg:\n")
# height = input("Zadaj výšku v metroch:\n")

# BMI = int(weight) / float(height)**2
# BMI = int(BMI)
# print("Vaše BMI je: ", str(BMI))

            # BMI index

weight = float(input("Zadaj váhu v kg:\n"))
height = float(input("Zadaj výšku v metroch:\n"))

BMI = weight / (height**2)

if BMI < 18.5:
    print(f"Vaše BMI je {(round(BMI, 1))}, máte podvýživu.")
elif BMI <= 24.9:
    print(f"Vaše BMI je {(round(BMI, 1))}, máte normálnu hmotnosť.")
elif BMI <= 29.9:
    print(f"Vaše BMI je {(round(BMI, 1))}, máte nadváhu.")
elif BMI <= 34.9:
    print(f"Vaše BMI je {(round(BMI, 1))}, máte obezitu.")
else:
    print(f"Vaše BMI je {(round(BMI, 1))}, máte extrémnu obezitu.")