from les_2 import *

p1 = persoon("Ben",35,"Luik")
p2=persoon("An",28,"Hasselt")
p3=persoon("Piet",32,"Genk")

dict_personen = {"per1":p1,"per2":p2,"per3":p3}

def toon_id_persoonsinfo():
    for id,persoon in dict_personen.items():
        print(id,persoon)

def voeg_persoon_toe(id, naam, leeftijd, woonplaats):
    per = persoon(naam,leeftijd,woonplaats)
    dict_personen[id] = per

def verwijder_persoon(id):
    toon_id_persoonsinfo()
    for per in dict_personen.keys():
        if per == id:
            dict_personen.pop(id)
            print("id verdijderd")
            return
    print("id niet gevonden")

def zoek_persoon():
    toon_id_persoonsinfo()
    naam = input("Geef naam: ")
    for per in dict_personen.values():
        if per.naam == naam:
            print("Gevonden")
            return
    print("Niet gevonden")

voeg_persoon_toe("per4","Jan",41,"Gent")

# toon_id_persoonsinfo()
zoek_persoon()