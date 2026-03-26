import random

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

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


autot = []
for i in range(10):
    huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i+1}", huippunopeus)
    autot.append(auto)

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False

print(f"{'Rekisteri':<10} {'Huippunopeus':<15} {'Nopeus':<10} {'Matka':<10}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<15} {auto.nopeus:<10} {int(auto.kuljettu_matka):<10}")