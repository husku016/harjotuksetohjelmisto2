class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0


auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", auto.nopeus, "km/h")
print("Kuljettu matka:", auto.kuljettu_matka, "km")

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print("Nopeus kiihdytysten jälkeen:", auto.nopeus, "km/h")

auto.kiihdyta(-200)

print("Nopeus hätäjarrutuksen jälkeen:", auto.nopeus, "km/h")