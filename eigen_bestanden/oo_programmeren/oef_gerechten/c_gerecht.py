class gerecht:
    def __init__(self,naam,omschrijving,prijs,soort):
        self.soort = soort
        self.prijs = prijs
        self.omschrijving = omschrijving
        self.naam = naam

    def __str__(self):
        return f"{self.naam}: {self.omschrijving} €{self.prijs}"