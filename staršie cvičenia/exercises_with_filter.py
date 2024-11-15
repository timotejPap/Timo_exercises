
cisla = [22, 68, -50, 32, -25]
zaporne = filter(lambda x: x < 0, cisla)
print(list(zaporne))

slova = ["ryba", "Igor", "macka", "pes", "Stefan"]
male_pismeno = filter(lambda x: x[0].islower(), slova)
print(list(male_pismeno))

udaje = ["Peter", 12, "x", 256, "jablko", 12.9]
je_cislo = filter(lambda x: isinstance(x, (int, float)), udaje)
print(list(je_cislo))