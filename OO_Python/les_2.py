class persoon:

    def __init__(self,naam,leeftijd,woonplaats):
        self.woonplaats = woonplaats
        self.leeftijd = leeftijd
        self.naam = naam

    def __str__(self):
        return f"{self.naam}\t{self.leeftijd}\t{self.woonplaats}"

    def stel_je_voor(self):
        return f"Hoi ik ben {self.naam}"

