class Personeel:

    def __init__(self,id,voornaam,achternaam,leeftijd,geslacht):
        self.geslacht = geslacht
        self.leeftijd = leeftijd
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.id = id

    @staticmethod
    def column_headers():
        headers = ["type(B/F)", "id", "voornaam","achternaam","leeftijd","geslacht","functie","vergoeding"]
        return headers

class Bediende(Personeel):
    def __init__(self, id, voornaam, achternaam, leeftijd, geslacht, functie, maandloon):
        super().__init__(id, voornaam, achternaam, leeftijd, geslacht)
        self.maandloon = maandloon
        self.functie = functie


    def __str__(self):
        print(f"{self.id} {self.voornaam} {self.achternaam}, {self.leeftijd}, {self.geslacht}, {self.functie}, {self.maandloon}")

class Freelance(Personeel):
    def __init__(self, id, voornaam, achternaam, leeftijd, geslacht, functie, uurloon):
        super().__init__(id, voornaam, achternaam, leeftijd, geslacht)
        self.uurloon = uurloon
        self.functie = functie
        

        