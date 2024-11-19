


class personen:
    headers= ["naam","leeftijd","woonplaats"]
    def __init__(self,naam,leeftijd,woonplaats):
        self.naam = naam
        self.leeftijd = leeftijd
        self.woonplaats = woonplaats

    def __str__(self):
        return f"{self.naam}, {self.leeftijd}, {self.woonplaats}"

    def add_person(self):
        new_person = []
        for i in personen.headers:
            keuze= input(f"Geef aub de {i}: ")
            new_person.append(keuze)
        data.append(new_person)
        return data


data = [
    personen("Jan", 25, "Genk"),
    personen("Sophie", 30, "Brugge"),
    personen("Thomas", 22, "Antwerpen"),
    personen("Elise", 27, "Gent"),
    personen("Bram", 35, "Leuven"),
    personen("Laura", 28, "Hasselt"),
    personen("Noah", 19, "Kortrijk"),
    personen("Emma", 33, "Mechelen"),
    personen("Liam", 29, "Oostende"),
    personen("Julie", 24, "Turnhout"),
    personen("Victor", 31, "Sint-Niklaas"),
    personen("Lotte", 26, "Aalst"),
    personen("Lucas", 23, "Genk"),
    personen("Charlotte", 32, "Brugge"),
    personen("Arthur", 21, "Gent")
]



