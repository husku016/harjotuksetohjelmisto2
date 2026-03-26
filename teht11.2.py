class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = nopeus

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

def main():
    s_auto = Sähköauto("ABC-15", 180, 52.5)
    p_auto = Polttomoottoriauto("ACD-123", 165, 32.3)

    s_auto.aseta_nopeus(150)
    p_auto.aseta_nopeus(140)

    s_auto.aja(3)
    p_auto.aja(3)

    print(f"Sähköauto {s_auto.rekisteritunnus} matkamittari: {s_auto.matkamittari} km")
    print(f"Polttomoottoriauto {p_auto.rekisteritunnus} matkamittari: {p_auto.matkamittari} km")

if __name__ == "__main__":
    main()