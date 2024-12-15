from functies import *

def main():
    """Hoofdmenu voor interactie."""
    while True:
        print("\nMenu:")
        print("1) Toon alle *KEUZE*")
        print("2) Voeg data toe")
        print("3) Pas aan")
        print("4) TBD")
        print("5) TBD")
        print("6) TBD")
        print("STOP) Stoppen")

        keuze = input("Maak een keuze: ").upper()
        if keuze == "STOP":
            print("Programma gestopt")
            break
        functies_dict[keuze]()

main()