class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def kerros_ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print("Hissi on kerroksessa", self.nykyinen)

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print("Hissi on kerroksessa", self.nykyinen)

    def siirry_kerrokseen(self, kohde):
        while self.nykyinen < kohde:
            self.kerros_ylos()
        while self.nykyinen > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit alas.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 3)

talo.palohalytys()