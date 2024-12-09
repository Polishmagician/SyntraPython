class Cursus:

    def __init__(self,id,naam,kostprijs):
        self.kostprijs = kostprijs
        self.naam = naam
        self.id = id

    def __str__(self):
        return f"{self.id}, {self.naam}, {self.kostprijs}"

