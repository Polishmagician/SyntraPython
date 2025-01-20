from functies import *


while True:
    print("\nMenu:")
    print("1) Toon alle wagens")
    print("2) Voeg wagen toe")
    print("3) Verwijder wagen")
    print("4) Toon wagen met brandstof")
    print("5) Update CSV")
    print("STOP) Stoppen")

    keuze = input("Wat wil je doen? ").upper()
    if keuze == "STOP":
        break
    dict_functies[keuze](data)