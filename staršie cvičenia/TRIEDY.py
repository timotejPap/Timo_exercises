class Auto(object):
    def __init__(self, znacka_auta, farba):
        self.nazov = znacka_auta
        self.farba = farba
        print("Toto je auto znacky", self.nazov, self.farba, "farby")

    def vpred (self):
        for i in range(3):
            print("Auto ide vpred")
        return

    def dozadu (self):
        for i in range(2):
            print("Auto ide dozadu")
        return

octavia = Auto(znacka_auta="Skoda", farba="bielej")
print(octavia.nazov)
octavia.vpred()
octavia.dozadu()

class Robot(object):
    def __init__(self, meno, farba):
        self.nazov = meno
        self.farba = farba
        print("Tu vznikne nas robot")

    def prava_ruka (self):
        for i in range(1):
            print("C-3PO zdvihol pravu ruku")
        return

    def lava_noha (self):
        for i in range(1):
            print("C-3PO vykrocil lavou nohou")
        return

c3po = Robot(meno="C-3PO", farba = "zlatej")
print("Nas robot je", c3po.nazov)
print(c3po.nazov, "je", c3po.farba, "farby")
print(c3po.prava_ruka())
print(c3po.lava_noha())

class R2_D2(Robot):

    def __init__(self):
        self.meno = "R2_D2"
        print("Vytvorili sme R2-D2")

    def vytvori_hologram(self):
        while True:
            prikaz = input("Co ma urobit R2_D2? ")
            if prikaz == ("Vytvor hologram!"):
                print(self.meno, "vytvoril hologram")
            elif prikaz == ("Chod vpred!"):
                print(self.meno, "isiel dopredu")
            else:
                print("Neznamy rozkaz!")

    def posun_vpred(self):
        for i in range(3):
            print("R2_D2 isiel 3 metre vpred")

hologram = R2_D2()
hologram.vytvori_hologram()
