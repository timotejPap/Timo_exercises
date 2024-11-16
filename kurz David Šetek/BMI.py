# BMI calculator


weight = input("Zadaj váhu v kg:\n")
height = input("Zadaj výšku v metroch:\n")

BMI = int(weight) / float(height)**2
BMI = int(BMI)
print("Vaše BMI je: ", str(BMI))