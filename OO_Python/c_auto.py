class auto:
    aantal_wagens = 0

    def __init__(self, merk, model, bouwjaar, brandstof):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.brandstof = brandstof
        auto.aantal_wagens += 1

    def __str__(self):
        return (f"Auto heeft merk {self.merk} en model {self.model}"
                f" het bouwjaar is {self.bouwjaar} en de brandstof is {self.brandstof}")

    def geef_terug_als_dict(self):
        return self.__dict__

    def hoeveel_wagens(self):
        return auto.aantal_wagens


a1 = auto("Citroën","Cactus",2015,"Benzine")
a2 = auto("Ford","Focus",2003,"Diesel")
a3 = auto("Tesla","Model Y",2022,"EV")
a4 = auto("Renault","Clio",2010,"Benzine")
a5 = auto("BMW","1 Series",2023,"Benzine")

print(a1)
