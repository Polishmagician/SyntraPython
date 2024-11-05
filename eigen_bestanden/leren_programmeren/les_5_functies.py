def toon_inhoud_lijst(lijst):
    for inhoud in lijst:
        print(inhoud)
def voeg_item_toe(lijst:list):
    item = input("Geef item: ")
    lijst.append(item)
    print(f"{item} is toegevoegd")
def verwijder_uit_lijst(lijst:list):
    item = input("Welk item wens je te verwijderen?")
    if item in lijst:
        lijst.remove(item)
        print(lijst)
    else:
        print(f"{item} niet in lijst")
def sorteer_lijst(lijst:list):
    methode = input("1 A-Z, 2 Z-A")
    if methode == "1":
        lijst.sort()
    elif methode == "2":
        lijst.sort(reverse=True)
    else:
        print("Commando is ongeldig")
    print(lijst)

def toon_overzicht_functies():
    print("1: Toon de lijst")
    print("2: Voeg een item toe")
    print("3: Verwijder een item")
    print("4: Sorteer de lijst")