class Persoon:

    def __init__(self,id,naam,leeftijd,woonplaats):
        self.woonplaats = woonplaats
        self.leeftijd = leeftijd
        self.naam = naam
        self.id = id
    def __str__(self):
        return f"{self.id}, {self.naam}, {self.leeftijd}, {self.woonplaats}"
    def __add__(self, other):
        return self.leeftijd + other.leeftijd #Returns int
    def __eq__(self, other):
        return self.leeftijd == other.leeftijd #Returns boolean

class Docent(Persoon):
    def __init__(self, id, naam, leeftijd, woonplaats,maandloon):
        super().__init__(id, naam, leeftijd, woonplaats)
        self.maandloon = maandloon
        self.cursussen = []
    def __str__(self):
        return f"{super.__str__()}, {self.maandloon}"
    def __add__(self, other):
        if isinstance(other,Docent):
            return self.maandloon + other.maandloon

class Cursist(Persoon):
    def __init__(self, id, naam, leeftijd, woonplaats,jaar_inschrijving):
        super().__init__(id, naam, leeftijd, woonplaats)
        self.jaar_inschrijving = jaar_inschrijving
        self.cursussen = []
    def __str__(self):
        return f"{super.__str__()}, {self.jaar_inschrijving}"




