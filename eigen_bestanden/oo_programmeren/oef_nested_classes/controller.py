from Classes import *
from data_wagens import *
from data_medewerkers import *
from functies import *


def controller():
    while True:
        print("1: Toon personeel",
              "2: Toon bediendes",
              "3: Toon arbeiders",
              "4: Toon wagens",
              "5: Voeg personeel toe",
              "6: Voeg wagen toe",
              "7: Ken bedrijfswagen toe aan bediende",
              "8: Verwijder personeelslid",
              "9: Verander loon",
              "10: Toon bedienden maandloon meer dan X",
              "11: Toon bedienden met bedrijfswagen",
              "STOP: Stop"
              )
        keuze = input("Maak je keuze: ")
        if keuze.upper() == "STOP":
            break
        keuze = int(keuze)
        if keuze in functie_dict:
            functie_dict[keuze]()


controller()
