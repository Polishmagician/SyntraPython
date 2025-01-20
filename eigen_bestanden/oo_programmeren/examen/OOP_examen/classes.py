class Wagen:

    def __init__(self, id, merk, model, bouwjaar, brandstof, huurprijs):
        self.huurprijs = huurprijs
        self.brandstof = brandstof
        self.bouwjaar = bouwjaar
        self.model = model
        self.merk = merk
        self.id = id

    @staticmethod #Aangemaakt om self niet te moeten roepen als arg in onderstaande functie
    def column_headers():
        headers = ["id", "merk","model","bouwjaar","brandstof","huurprijs"]
        return headers

