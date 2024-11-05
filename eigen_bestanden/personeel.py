# Maak een 2d lijst personeel met 5  rijen aan data.
# Naam, Leeftijd, Woonplaats, Functie, Afdeling
# Toon deze data in een tabulate tabel
# Zorg ervoor dat een rij toegevoegd kan worden
# Zorg ervoor dat een rij verwijderd kan worden
# Maak een functie sorteren op naam en sorteren op leeftijd

from tabulate import tabulate

personeelsleden =  {
    1:{
        "Naam": "Jeroen van Dijk",
        "Leeftijd": 34,
        "Woonplaats": "Amsterdam",
        "Functie": "Projectmanager",
        "Afdeling": "ICT"
    },
    2:{
        "Naam": "Sanne de Vries",
        "Leeftijd": 29,
        "Woonplaats": "Rotterdam",
        "Functie": "HR-Adviseur",
        "Afdeling": "HR"
    },
    3:{
        "Naam": "Mark Jansen",
        "Leeftijd": 45,
        "Woonplaats": "Utrecht",
        "Functie": "Financieel Analist",
        "Afdeling": "Financiën"
    },
    4:{
        "Naam": "Nina Bakker",
        "Leeftijd": 38,
        "Woonplaats": "Den Haag",
        "Functie": "Marketing Coördinator",
        "Afdeling": "Marketing"
    },
    5:{
        "Naam": "Thomas Willems",
        "Leeftijd": 50,
        "Woonplaats": "Eindhoven",
        "Functie": "Technisch Ingenieur",
        "Afdeling": "Productie"
    }}


kolom = ["ID", "Naam", "Leeftijd", "Woonplaats", "Functie", "Afdeling"]

def create_list(personeel):
    personeel_list = []
    for key, inner in personeel.items():
        row = [key]
        for k,v in inner.items():
            row.append(v)
        personeel_list.append(row)
    return personeel_list


def add_personnel(personeel,personeel_list):
    new_personnel = [max(personeel.keys())+1,
                     input("Geef de naam: "),
                     int(input("Geef de leeftijd: ")),
                     input("Geef de woonplaats: "),
                     input("Geef de functie: "),
                     input("Geef de afdeling: ")]
    personeel_list.append(new_personnel)
    return personeel_list

def remove_personnel(personeelsleden,personeel_list):
    id_to_remove = int(input("Geef het ID dat je wilt verwijderen: "))
    if id_to_remove in personeelsleden.keys():
        del personeelsleden[id_to_remove]
        create_list(personeelsleden)
        return
    else:
        print(f"{id_to_remove} is geen geldige ID")

def wijzig_item(personeelsleden):
    id = int(input("Welk ID wil je wijzigen? "))
    keys = ["Naam","Leeftijd","Woonplaats","Functie","Afdeling"]
    for item in keys:
        print(item)
    veld = input("Welk veld wil je wijzigen? (Typ uit lijst hierboven)" )
    if veld in keys:
        new_veld = input("In wat wil je het wijzigen? ")
        personeelsleden[id][veld] = new_veld
    else:
        print(f"{veld} is geen geldige keuze")

def sort_leeftijd(personeelsleden):  #Ik maak hier een lijst, maar mijn create maakt van een dict een lijst. Ik moet die create lijst eens herbekijken of dat wel nodig is
    sorted_list = sorted(personeelsleden.items(), key = lambda item: item[1]["Naam"])
    return sorted_list

def controller(personeelsleden):
    keuze = ""
    while keuze != "6":
        print("1: Toon de huidige tabel", "2: Voeg een ID toe", "3: Verwijder een ID", "4: Wijzig een veld","5: Sorteer op leeftijd", "6: STOP")
        keuze = input("Wat wil je doen? ")
        if keuze == "1":
            pass
        elif keuze == "2":
            add_personnel(personeelsleden, create_list(personeelsleden))
        elif keuze == "3":
            remove_personnel(personeelsleden, create_list(personeelsleden))
        elif keuze == "4":
            wijzig_item(personeelsleden)
        elif keuze == "5":
            sort_leeftijd(personeelsleden)
        print(tabulate(create_list(personeelsleden), headers=kolom))
controller(personeelsleden)