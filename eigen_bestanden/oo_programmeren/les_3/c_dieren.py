class dier():
    def __init__(self,naam,leeftijd):
        self.leeftijd = leeftijd
        self.naam = naam
    def __str__(self):
        return f"naam: {self.naam}, leeftijd : {self.leeftijd}"

class hond(dier):
    def __init__(self, naam, leeftijd, ras):
        super().__init__(naam, leeftijd)
        self.ras = ras
    def __str__(self):
        return f"{super().__str__()} en ras : {self.ras}"

d=dier("Foxy",7)
print(d)

h=hond("Foxy",7,"Border Collie")
print(h)

#Opzoeken: Diamond probleem