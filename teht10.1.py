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


h = Hissi(1, 10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)