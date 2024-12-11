class boek():
    def __init__(self,id,titel,aantal_paginas,auteur):
        self.auteur = auteur
        self.aantal_paginas = aantal_paginas
        self.titel = titel
        self.id = id

    def __str__(self):
        return f"{self.id}, {self.auteur}, {self.titel}, {self.aantal_paginas}"

    headers = ["id", "auteur", "titel", "paginas"]

class auteur():
    def __init__(self,id,voornaam,achternaam,nationaliteit):
        self.nationaliteit = nationaliteit
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.id = id

    def __str__(self):
        return f"{self.id}, {self.voornaam}, {self.achternaam}, {self.nationaliteit}"

    headers = ["id", "voornaam", "achternaam", "nationaliteit"]


class lezer():
    def __init__(self,id,voornaam,achternaam,gemeente,geslacht):
        self.geslacht = geslacht
        self.gemeente = gemeente
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.id = id

    def __str__(self):
        return f"{self.id}, {self.voornaam}, {self.achternaam}, {self.gemeente}, {self.geslacht}"

    headers = ["id", "voornaam", "achternaam", "gemeente", "geslacht"]


class uitleningen():
    def __init__(self,id,boek,lezer):
        self.lezer = lezer
        self.boek = boek
        self.id = id

    def __str__(self):
        return f"{self.id}, {self.boek}, {self.lezer}"

    headers = ["id", "boek", "lezer"]

        