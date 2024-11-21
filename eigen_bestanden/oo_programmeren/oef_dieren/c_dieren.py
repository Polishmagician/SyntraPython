class dier:

    def __init__(self, naam, soort, leeftijd, geslacht):
        self.geslacht = geslacht
        self.leeftijd = leeftijd
        self.soort = soort
        self.naam = naam

    def __str__(self):
        return f"{self.naam} is een {self.soort}, {self.leeftijd} jaar en {self.geslacht}"
