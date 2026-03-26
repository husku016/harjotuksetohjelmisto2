class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")

def main():
    julkaisu1 = Lehti("Aku Ankka", "Aki Hyyppä")
    julkaisu2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    julkaisu1.tulosta_tiedot()
    print()
    julkaisu2.tulosta_tiedot()

if __name__ == "__main__":
    main()