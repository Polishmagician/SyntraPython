from Classes import *
from data_wagens import *
from data_medewerkers import *
from functies import *


def controller():
    last_keuze = 0
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
              "12: Wegschrijven naar CSV",
              "'STOP': Stop"
              )
        keuze = input("Maak je keuze: ")
        if keuze.upper() == "STOP":
            break
        elif keuze == "12":
            datasets = [personeel_data_class, bedienden_data_class, arbeiders_data_class, wagens]
            if last_keuze < 5:
                wegschrijven(datasets[last_keuze-1])
        keuze = int(keuze)
        if keuze in functie_dict:
            functie_dict[keuze]()
        last_keuze = keuze


controller()
