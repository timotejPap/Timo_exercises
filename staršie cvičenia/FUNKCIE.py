# PRIKLAD
# definovaná funkcia
def vypocitaj (x, z):
    delene = x/z
    return delene

# hlavny program
priklad = vypocitaj (100, 5)
print("Vysledok je", priklad)

# FUNKCIA SO SLOVNIKOM
def osoba (meno, priezvisko, titul="Mgr."):
    return titul, meno, priezvisko

ja = osoba("Timotej", "Pap")
print("Ja som", ja)

ona = osoba("Daniela", "Papová")
print("Moja manželka je", ona)

def regale (slovnik: dict, kluc: str):
    print("Obsah satnika je: ")
    for i in satnik[kluc]:
        print(i)
