
"""class R2_D2(object):

    def __init__(self):
        self.meno = "R2_D2"
        print("Vytvorili sme R2-D2")

    def vytvori_hologram(self):
        while True:
            prikaz = input("Co ma urobit R2_D2? ")
            if prikaz == ("Vytvor hologram!"):
                print(self.meno, "vytvoril hologram")
            #else:
                #print("Neznamy rozkaz!")

            elif prikaz == ("Chod vpred!"):
                print(self.meno, "isiel dopredu")
            else:
                print("Neznamy rozkaz!")


hologram = R2_D2()
hologram.vytvori_hologram()
"""

"""
pismena = ("T", "i", "m", "o")
for i in pismena:
    print(i)
    print("Ahoj")
    if i == "m":
        print("Je to m")
    print("Vsade vypise")

import sys
print(sys.version)

from platform import python_version

print("Current Python Version-", python_version())
print(sys.version_info.minor)


firstNumber = 2
secondNumber = 3
secondNumber = secondNumber + firstNumber
thirdNumber = firstNumber * secondNumber
print(thirdNumber + secondNumber)
"""

def print_concatenate(a, b):
    concatenate = (a + b)
    return concatenate

"""
print_concatenate("hello ", "world")  # Vypise hello world
print_concatenate("informatika", "101")  # Vypise informatika101
"""

spolu = print_concatenate("Ahoj ", "svet")
print(spolu)