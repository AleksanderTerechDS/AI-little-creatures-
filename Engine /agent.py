import random


class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.energia = 100
        self.zyje = True

    def rusz_sie(self, max_x, max_y):
        if not self.zyje:
            return

        # Ruch o 1 pole w dowolną stronę
        self.x = max(0, min(max_x, self.x + random.choice([-1, 0, 1])))
        self.y = max(0, min(max_y, self.y + random.choice([-1, 0, 1])))

        # Koszt życia
        self.energia -= 1
        if self.energia <= 0:
            self.zyje = False

    def zjedz(self, wartosc):
        self.energia += wartosc