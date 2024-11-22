class personeel:
    id_personeel = 0
    def __init__(self,id,naam,leeftijd,geslacht, functie):
        self.naam = naam
        self.leeftijd = leeftijd
        self.geslacht = geslacht
        self.functie = functie
        personeel.id_personeel += 1
        self.id = id

    def __str__(self):
        return f"{self.id_personeel}: {self.naam} is een {self.geslacht} en {self.leeftijd} jaar"


class bediende(personeel):
    def __init__(self, id,naam, leeftijd, geslacht,functie, maandloon, afdeling,bedrijfswagen=None):
        super().__init__(id,naam, leeftijd, geslacht,functie)
        self.maandloon = maandloon
        self.afdeling = afdeling
        self.bedrijfswagen = bedrijfswagen
        personeel.id_personeel -= 1

    def __str__(self):
        return f"{super().__str__()}, verdient {self.maandloon} per maand en werkt in de afdeling {self.afdeling}"

class arbeider(personeel):

    def __init__(self, id,naam, leeftijd, geslacht, functie, uurloon, uren_gewerkt):
        super().__init__(id,naam,leeftijd,geslacht,functie)
        self.uurloon = uurloon
        self.aantal_uur = uren_gewerkt
        personeel.id_personeel -= 1
    def __str__(self):
        return f"{super().__str__()}, verdient {self.uurloon} per uur en werkt {self.aantal_uur} uur"

class bedrijfswagen:
    id_wagen = 0
    def __init__(self,id,merk,model,bouwjaar, eigenaar = None):
        self.id = id
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.eigenaar = eigenaar
        bedrijfswagen.id_wagen += 1

