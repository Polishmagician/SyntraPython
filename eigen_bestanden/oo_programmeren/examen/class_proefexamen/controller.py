from functies import *


while True:
    print("\nMenu:")
    print("1) Toon alle medewerkers")
    print("2) Voeg data toe")
    print("3) Verwijder rij")
    print("4) Filter op maandloon hoger dan X")
    print("5) Filter op functie")
    print("STOP) Stoppen")

    keuze = input("Wat wil je doen? ").upper()
    if keuze == "STOP":
        break
    dict_functies[keuze](data)

