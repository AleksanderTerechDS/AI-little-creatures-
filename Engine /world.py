import random

class Swiat:
    def __init__(self, szerokosc=50, wysokosc=50):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.jedzenie = [] # Lista krotek (x, y)

    def generuj_jedzenie(self, ilosc=5):
        for _ in range(ilosc):
            x = random.randint(0, self.szerokosc)
            y = random.randint(0, self.wysokosc)
            self.jedzenie.append((x, y))

    def sprawdz_jedzenie(self, agent):
        # Jeśli agent stanie na jedzeniu, zjada je
        pozycja = (agent.x, agent.y)
        if pozycja in self.jedzenie:
            self.jedzenie.remove(pozycja)
            agent.zjedz(20) # Bonus do energii
            return True
        return False